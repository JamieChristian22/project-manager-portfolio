"""Reproduce portfolio controls without third-party dependencies."""
from pathlib import Path
import csv
import json
import re
import sqlite3
import sys
import zipfile
import xml.etree.ElementTree as ET
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def records(path):
    with Path(path).open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def load_case(folder):
    return {p.stem: records(p) for p in folder.glob('*.csv')}

def evaluate(data):
    errors = []
    required = ['requirements','tasks','tests','evidence','issues','decisions','actions','gates','budget']
    for name in required:
        if not data.get(name):
            errors.append(f'{name}: missing or empty table')
    if errors:
        return {'errors': errors, 'gate': 'HOLD'}
    maps = {}
    for name in required:
        key = 'cost_id' if name == 'budget' else 'id'
        ids = [r.get(key, '') for r in data[name]]
        if '' in ids or len(set(ids)) != len(ids):
            errors.append(f'{name}: missing or duplicate identifier')
        maps[name] = {r[key]: r for r in data[name]}
    def ref(row, field, table, multi=False, optional=False):
        value = row.get(field, '')
        if optional and not value:
            return
        values = value.split(';') if multi else [value]
        for v in values:
            if v not in maps[table]:
                errors.append(f'{row.get("id", row.get("cost_id"))}: invalid {field} {v!r}')
    for name in ['requirements','tasks','issues','actions']:
        for r in data[name]:
            if not r.get('owner','').strip(): errors.append(f'{r["id"]}: missing owner')
    for r in data['tasks']:
        ref(r,'requirement_id','requirements')
        ref(r,'predecessors','tasks',True,True)
        if r['status'] not in ['Complete','In progress','Not started']: errors.append(f'{r["id"]}: invalid task status')
        if r['status']=='Complete': ref(r,'evidence','evidence')
    for r in data['tests']:
        ref(r,'requirement_id','requirements'); ref(r,'task_id','tasks')
        if r['task_id'] in maps['tasks'] and maps['tasks'][r['task_id']]['requirement_id'] != r['requirement_id']:
            errors.append(f'{r["id"]}: task and requirement mismatch')
        if r['result'] not in ['Pass','Fail','Not run','Blocked']: errors.append(f'{r["id"]}: invalid test result')
        if r['result']=='Pass':
            ref(r,'evidence','evidence')
            if not r['observed_result'].strip() or r['observed_result']=='Not yet evaluated': errors.append(f'{r["id"]}: pass lacks observation')
    for r in data['issues']:
        ref(r,'task_id','tasks'); ref(r,'decision_id','decisions')
        if r['severity'] not in ['Low','Medium','High','Critical']: errors.append(f'{r["id"]}: invalid severity')
        if r['status'] not in ['Open','Closed']: errors.append(f'{r["id"]}: invalid issue status')
        if r['status']=='Closed': ref(r,'closure_evidence','evidence')
    for r in data['actions']:
        ref(r,'issue_id','issues');ref(r,'task_id','tasks')
        if r['status'] not in ['Open','Complete']: errors.append(f'{r["id"]}: invalid action status')
        if r['status']=='Complete': ref(r,'closure_evidence','evidence')
    for r in data['decisions']:
        ref(r,'issue_id','issues')
        if not r['approver'].strip(): errors.append(f'{r["id"]}: missing approver')
        if r['status'] not in ['Proposed','Approved','Rejected']: errors.append(f'{r["id"]}: invalid decision status')
        if r['status']=='Approved' and not r['decision_day'].isdigit(): errors.append(f'{r["id"]}: missing approval day')
    for r in data['gates']:
        ref(r,'requirement_ids','requirements',True);ref(r,'decision_id','decisions')
        if not r['approver'].strip(): errors.append(f'{r["id"]}: missing approver')
        if r['approval'] not in ['Pending','Approved','Rejected']: errors.append(f'{r["id"]}: invalid gate approval')
        if r['approval']=='Approved' and not r['approval_day'].isdigit(): errors.append(f'{r["id"]}: missing gate approval day')
        mandatory={x['id'] for x in data['requirements'] if x['mandatory']=='yes'}
        if not mandatory <= set(r['requirement_ids'].split(';')): errors.append(f'{r["id"]}: mandatory requirements omitted')
    for r in data['requirements']:
        if r['mandatory'] not in ['yes','no']: errors.append(f'{r["id"]}: invalid mandatory flag')
        if not r['acceptance'].strip(): errors.append(f'{r["id"]}: missing acceptance criterion')
        if not any(t['requirement_id']==r['id'] for t in data['tests']): errors.append(f'{r["id"]}: no test coverage')
    for name in ['tasks','actions','issues']:
        for r in data[name]:
            if not r['due_day'].isdigit(): errors.append(f'{r["id"]}: invalid due day')
    # Forward pass with explicit cycle detection.
    schedule={}; visiting=set(); order=[]
    def visit(key):
        if key in schedule:return schedule[key]['finish']
        if key in visiting:raise ValueError(f'schedule cycle at {key}')
        visiting.add(key);r=maps['tasks'][key]
        duration=int(r['duration_days'])
        if duration<=0:raise ValueError(f'{key}: duration must be positive')
        preds=[x for x in r['predecessors'].split(';') if x]
        start=max((visit(p) for p in preds),default=0)
        schedule[key]={'start':start,'finish':start+duration,'duration':duration}
        visiting.remove(key);order.append(key)
        return start+duration
    try:
        finish=max(visit(k) for k in maps['tasks'])
        for key in reversed(order):
            successors=[k for k,r in maps['tasks'].items() if key in r['predecessors'].split(';')]
            late_finish=min((schedule[k]['late_start'] for k in successors),default=finish)
            schedule[key]['late_start']=late_finish-schedule[key]['duration']
            schedule[key]['float']=schedule[key]['late_start']-schedule[key]['start']
    except (ValueError,KeyError) as exc:
        errors.append(str(exc));finish=None
    baseline=changes=actual=etc=0
    for r in data['budget']:
        ref(r,'task_id','tasks')
        try:
            b,c,a,e=[float(r[k]) for k in ['baseline_usd','approved_change_usd','actual_usd','etc_usd']]
            if min(b,a,e)<0: errors.append(f'{r["cost_id"]}: negative baseline, actual or ETC')
            if c:
                ref(r,'change_reference','decisions')
                if maps['decisions'].get(r['change_reference'],{}).get('status')!='Approved': errors.append(f'{r["cost_id"]}: unauthorized budget change')
            baseline+=b;changes+=c;actual+=a;etc+=e
        except (ValueError,KeyError): errors.append(f'{r["cost_id"]}: invalid cost')
    passed=sum(r['result']=='Pass' for r in data['tests'])
    executed=sum(r['result'] in ['Pass','Fail'] for r in data['tests'])
    blocking=sum(r['status']!='Closed' and r['severity'] in ['High','Critical'] for r in data['issues'])
    open_actions=sum(r['status']!='Complete' for r in data['actions'])
    mandatory_pass=all(any(t['requirement_id']==r['id'] for t in data['tests']) and all(t['result']=='Pass' for t in data['tests'] if t['requirement_id']==r['id']) for r in data['requirements'] if r['mandatory']=='yes')
    approvals=all(r['approval']=='Approved' and maps['decisions'].get(r['decision_id'],{}).get('status')=='Approved' for r in data['gates'])
    variance=baseline+changes-actual-etc
    reasons=[]
    if errors:reasons.append('Invalid or missing source records')
    if not mandatory_pass:reasons.append('Mandatory testing incomplete or failed')
    if any(r['status']!='Complete' for r in data['tasks']):reasons.append('Required tasks incomplete')
    if blocking:reasons.append(f'{blocking} open high/critical issue(s)')
    if open_actions:reasons.append(f'{open_actions} open action(s)')
    if not approvals:reasons.append('Authorized gate decision pending')
    if variance<0:reasons.append('Forecast exceeds authorized exercise budget')
    return dict(errors=errors,schedule=schedule,finish=finish,baseline=baseline,changes=changes,actual=actual,etc=etc,forecast=actual+etc,variance=variance,passed=passed,executed=executed,tests=len(data['tests']),gate='HOLD' if reasons else 'READY',reasons=reasons)

def workbook_scan(path):
    with zipfile.ZipFile(path) as z:
        sheets=[x.attrib['name'] for x in ET.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',NS)]
        formulas=missing=0;errors=[]
        for n in z.namelist():
            if n.startswith('xl/worksheets/sheet') and n.endswith('.xml'):
                for c in ET.fromstring(z.read(n)).findall('.//m:c',NS):
                    f=c.find('m:f',NS);v=c.find('m:v',NS)
                    if f is not None:
                        formulas+=1
                        if v is None or v.text is None:missing+=1
                        if '#REF!' in (f.text or ''):errors.append(f'{n}:{c.attrib["r"]} broken reference')
                    if c.attrib.get('t')=='e':errors.append(f'{n}:{c.attrib["r"]} {v.text if v is not None else "error"}')
        return dict(sheets=sheets,formulas=formulas,missing_caches=missing,errors=errors)

def check_links(root):
    errors=[]
    for p in root.rglob('*.md'):
        if '.git' in p.parts or p.name=='Previous_Overview.md':continue
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            target=target.split(' "')[0].strip('<>')
            if re.match(r'^(?:https?://|mailto:|#)',target):continue
            dest=unquote(target.split('#')[0])
            if dest and not (p.parent/dest).exists():errors.append(f'{p.relative_to(root)}: {target}')
    return errors

def source_analytics(root):
    out=[];errors=[]
    for project in root.iterdir():
        if not project.is_dir():continue
        csvs=list(project.glob('*.csv'));sqls=list(project.glob('*.sql'))
        if not csvs or not sqls:continue
        con=sqlite3.connect(':memory:')
        for p in csvs:
            rr=records(p)
            if not rr:continue
            fields=list(rr[0]); defs=[]
            for k in fields:
                numeric=all(re.fullmatch(r'-?\d+(\.\d+)?',r[k] or '') for r in rr)
                defs.append('"'+k+'" '+('REAL' if numeric else 'TEXT'))
            con.execute(f'CREATE TABLE "{p.stem}" ({",".join(defs)})')
            con.executemany(f'INSERT INTO "{p.stem}" VALUES ({",".join("?" for _ in fields)})', [[r[k] for k in fields] for r in rr])
            if len({r.get('week') for r in rr})!=len(rr):errors.append(f'{p}: duplicate week')
        for p in sqls:
            statements=[s.strip() for s in re.sub(r'--[^\n]*','',p.read_text()).split(';') if s.strip()]
            try:
                counts=[len(con.execute(s).fetchall()) for s in statements]
                out.append(f'| {p.relative_to(root)} | {len(counts)} | {", ".join(map(str,counts))} |')
            except sqlite3.Error as exc:errors.append(f'{p.relative_to(root)}: {exc}')
        con.close()
    return out,errors

def main():
    report=['# Portfolio verification report','', 'Generated from repository inputs by `python scripts/validate_portfolio.py`. This is a structural and arithmetic check, not native Excel recalculation or proof of real project execution.','', '## Linked exercise results','', '| Project | Finish day | Forecast | Favorable variance | Required tests passed | Gate |','|---|---:|---:|---:|---:|---|']
    failures=[]
    for folder in sorted(ROOT.glob('*/Control_Exercise')):
        result=evaluate(load_case(folder));failures.extend(f'{folder.parent.name}: {e}' for e in result['errors'])
        if 'forecast' not in result:continue
        r=result
        report.append(f'| {folder.parent.name} | {r["finish"]} | ${r["forecast"]:,.0f} | ${r["variance"]:,.0f} | {r["passed"]}/{r["tests"]} | {r["gate"]} |')
        lines=['# Calculated exercise status','', '**Fictional supplemental exercise; not original project results.**','',f'**Release: {r["gate"]}.** '+ '; '.join(r['reasons'])+'.','',f'Authorized budget: ${r["baseline"]+r["changes"]:,.0f}. Actual: ${r["actual"]:,.0f}. ETC: ${r["etc"]:,.0f}. Forecast: ${r["forecast"]:,.0f}. Favorable variance: ${r["variance"]:,.0f}.','',f'Testing: {r["executed"]}/{r["tests"]} executed; {r["passed"]}/{r["tests"]} required tests passed.','', '| Task | Early start | Early finish | Total float | Critical |','|---|---:|---:|---:|---|']
        for key,s in sorted(r['schedule'].items()):lines.append(f'| {key} | {s["start"]} | {s["finish"]} | {s.get("float","—")} | {"Yes" if s.get("float")==0 else "No"} |')
        lines+=['','Day 0 origin; business-day durations; finish-to-start dependencies; no holiday calendar or resource leveling. Float assumes the computed earliest project finish. Overlapping recovery activities cannot be added together.']
        (folder/'Calculated_Status.md').write_text('\n'.join(lines)+'\n')
    report+=['','HOLD is the expected result for the deliberately incomplete exercises. Passing validation means the records are consistent, not that a release is authorized.','','## Workbook structural scan','','| Workbook | Sheets | Formula cells | Missing caches | Stored errors / broken refs |','|---|---:|---:|---:|---:|']
    for p in sorted(ROOT.rglob('*.xlsx')):
        r=workbook_scan(p);failures.extend(f'{p.relative_to(ROOT)}: {e}' for e in r['errors'])
        report.append(f'| {p.relative_to(ROOT)} | {len(r["sheets"])} | {r["formulas"]} | {r["missing_caches"]} | {len(r["errors"])} |')
    report+=['','Zero formula cells means a static snapshot. A populated cache is a saved value, not independent recalculation proof. Native Excel rendering and input-change testing were not performed. Read [metric qualifications](../docs/METRICS_AND_EVIDENCE.md) before interpreting reserve, EVM or adoption figures.']
    queryrows,queryerrors=source_analytics(ROOT);failures+=queryerrors
    if queryrows:report+=['','## Original SQL execution','','SQLite execution against supplied CSVs. This verifies executable queries; it does not validate a production dataset.','','| SQL file | Statements | Rows returned per statement |','|---|---:|---|']+queryrows
    report+=['','## Local link validation','']
    failures+=check_links(ROOT)
    report.append('Local Markdown file destinations: '+('PASS' if not failures else 'See failures below')+'. Historical Previous_Overview.md is excluded and clearly labeled as superseded.')
    report+=['','## Result','',f'Validation errors: **{len(failures)}**.']
    report += ['- '+x for x in failures]
    (ROOT/'verification').mkdir(exist_ok=True)
    (ROOT/'verification/REPORT.md').write_text('\n'.join(report)+'\n')
    print('\n'.join(failures) if failures else 'PASS: source records, schedules, budgets, links, workbook structural scan and available SQL checks')
    return 1 if failures else 0

if __name__=='__main__':sys.exit(main())
