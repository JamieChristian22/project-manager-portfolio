"""Independent source arithmetic. Reads XLSX XML; never edits a workbook."""
from pathlib import Path
import csv
import json
import zipfile
import xml.etree.ElementTree as E

ROOT=Path(__file__).resolve().parents[1]
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def sheet(path,name):
    with zipfile.ZipFile(path) as z:
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            strings=[''.join(x.itertext()) for x in E.fromstring(z.read('xl/sharedStrings.xml'))]
        entries=E.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',NS)
        chosen=next(s for s in entries if s.attrib['name']==name)
        rid=chosen.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
        relationships=E.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        target=next(x.attrib['Target'] for x in relationships if x.attrib['Id']==rid)
        target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
        cells={}
        for c in E.fromstring(z.read(target)).findall('.//m:c',NS):
            value=c.findtext('m:v',default='',namespaces=NS)
            if c.attrib.get('t')=='s':value=strings[int(value)]
            elif c.attrib.get('t')=='inlineStr':value=''.join(c.find('m:is',NS).itertext())
            elif c.attrib.get('t') not in ['str','e'] and value:
                try:value=float(value)
                except ValueError:pass
            cells[c.attrib['r']]=value
        return cells

def read_csv(path):
    with path.open(newline='') as f:return list(csv.DictReader(f))

def main():
    lines=['# Original source reconciliation','', 'Independent arithmetic from the supplied CSVs and workbook source cells. Original workbook formula execution is outside this check. These results describe original simulations, not the separate control exercises.','']
    construction=ROOT/'Corporate_Construction_PM_Portfolio_Project'
    if construction.exists():
        p=construction/'04_Construction_PM_Project_Controls.xlsx'
        budget=sheet(p,'Budget_Cost');changes=sheet(p,'Change_Log');evm=sheet(p,'Earned_Value')
        lines+=['## Construction cost bridge','', '| Cost code | Budget revision | Logged approved changes | Unmapped difference |','|---|---:|---:|---:|']
        csvrows=[]
        for row in range(2,17):
            code=budget[f'A{row}'];revision=budget[f'D{row}']
            logged=sum(changes.get(f'G{r}',0) for r in range(2,14) if changes.get(f'I{r}')==code and changes.get(f'H{r}')=='Approved')
            delta=revision-logged
            lines.append(f'| {code} | ${revision:,.0f} | ${logged:,.0f} | ${delta:,.0f} |')
            csvrows.append(dict(cost_code=code,budget_revision_usd=revision,logged_approved_change_usd=logged,unmapped_difference_usd=delta))
        net=sum(r['budget_revision_usd'] for r in csvrows);logged=sum(r['logged_approved_change_usd'] for r in csvrows)
        original=sum(budget[f'C{r}'] for r in range(2,17));actual=sum(budget[f'G{r}'] for r in range(2,17));etc=sum(budget[f'H{r}'] for r in range(2,17))
        lines += ['',f'Original budget **${original:,.0f}** + net budget revisions **${net:,.0f}** = revised budget **${original+net:,.0f}**. Actual **${actual:,.0f}** + ETC **${etc:,.0f}** = forecast **${actual+etc:,.0f}**. Forecast headroom is **${original+net-actual-etc:,.0f}**.', '',f'The change log records **${logged:,.0f}** approved. Net budget revisions differ by **${net-logged:,.0f}**. The budget includes a **$420,000 contingency reduction**, but the source does not identify which changes were funded by reserve transfers or other authorizations. Do not invent a funding bridge or call this reconciled. The row-level differences above are the reconciliation worklist.','', '### Required control response','', 'Finance and the PM must map each change ID to cost code, gross amount, funding source, reserve draw, approval and posting date. Obtain the authorization behind budget-only adjustments, explain log-only amounts, and reconcile the register before approving additional discretionary changes. The original snapshot is retained; these differences are visible rather than silently overwritten.','', '### Earned value versus management forecast','']
        pv,ev,ac=[evm[k] for k in ['K5','K6','K7']];bac=evm['K4']
        lines += [f'PV ${pv:,.0f}; EV ${ev:,.0f}; AC ${ac:,.0f}; SPI **{ev/pv:.4f}**; CPI **{ev/ac:.4f}**. CPI-based EAC is **${bac/(ev/ac):,.0f}**, while the bottom-up management forecast is **${actual+etc:,.0f}**. The methods differ by **${actual+etc-bac/(ev/ac):,.0f}**. A productivity-based extrapolation and a remaining-cost forecast are not interchangeable. Explain future cost assumptions before selecting a forecast.', '', 'Average task progress is also not earned-value progress. The workbook’s unweighted activity averages should not be used as EV/BAC or converted directly into days of delay.']
        with (construction/'Change_Bridge.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(csvrows[0]),lineterminator="\n");w.writeheader();w.writerows(csvrows)
    else:
        lines+=['## Base-budget reconciliation','', '| Project | Baseline | Actual | Favorable variance | Variance % |','|---|---:|---:|---:|---:|']
        for project in sorted(ROOT.iterdir()):
            paths=[p for p in project.glob('*Project_Dashboard.xlsx') if p.name!='Project_Dashboard.xlsx'] if project.is_dir() else []
            if not paths:continue
            b=sheet(paths[0],'Budget');rows=[]
            for i in range(2,20):
                if isinstance(b.get(f'B{i}'),float) and isinstance(b.get(f'C{i}'),float) and b.get(f'A{i}') not in ['Total','Contingency','Remaining Contingency']:
                    rows.append(i)
            baseline=sum(b[f'B{i}'] for i in rows);actual=sum(b[f'C{i}'] for i in rows)
            lines.append(f'| {project.name} | ${baseline:,.0f} | ${actual:,.0f} | ${baseline-actual:,.0f} | {(baseline-actual)/baseline:.2%} |')
        e=read_csv(ROOT/'E-Commerce_Platform_Launch/project_metrics.csv')
        planned=sum(int(r['tasks_planned']) for r in e);done=sum(int(r['tasks_completed']) for r in e)
        due=sum(int(r['milestones_due']) for r in e);met=sum(int(r['milestones_completed']) for r in e)
        h=read_csv(ROOT/'Hospital_Intake_Workflow_Optimization/intake_metrics.csv')
        g=ROOT/'Global_Leadership_Training_Rollout/Global_Leadership_Training_Rollout_Project_Dashboard.xlsx'
        reg=sheet(g,'Regional Rollout')
        target=sum(reg[f'B{r}'] for r in range(2,6));registered=sum(reg[f'C{r}'] for r in range(2,6));attended=sum(reg[f'D{r}'] for r in range(2,6));completed=sum(reg[f'E{r}'] for r in range(2,6))
        lines+=['','## E-commerce reporting populations','',f'The weekly CSV sums to **{done}/{planned} ({done/planned:.2%})** task delivery. The final week is **24/24 (100%)**. The workbook Task Tracker is a separate ten-item deliverable list, so its 100% closeout is not the same denominator. Weekly milestones are **{met}/{due} ({met/due:.2%})** within the reported weekly rows. A late milestone can later close; weekly delivery and final closure must be labeled separately.','', 'Velocity rises from 24 to 48 in the synthetic series. Without a stable point-estimation scale and capacity history this is not evidence of a 100% productivity gain. Open issue counts are snapshots; do not sum them as distinct issues.','', '## Hospital intake','', f'Registration-time reduction: **{(float(h[0]["avg_registration_min"])-float(h[-1]["avg_registration_min"]))/float(h[0]["avg_registration_min"]):.2%}**. Wait-time reduction: **{(float(h[0]["avg_wait_min"])-float(h[-1]["avg_wait_min"]))/float(h[0]["avg_wait_min"]):.2%}**. These compare weekly averages in the simulation. Patient-level timestamps, medians, tail wait times, and comparable case mix would be needed to validate an operational claim.','', '## Leadership training denominator bridge','',f'Regional roster: {target:,.0f} targeted, {registered:,.0f} registered, {attended:,.0f} attended, {completed:,.0f} completed. Attendance / registered = **{attended/registered:.2%}**. Completed / attended = **{completed/attended:.2%}**. Completed / target = **{completed/target:.2%}**. These are three distinct measures.','', 'The weekly CSV describes a separate activity series and does not reconcile to unique regional participants. Do not total weekly attendees into the regional headcount. Without person-level keys, deduplicated program completion cannot be independently reconstructed from weekly activity alone.','', '## Salesforce readiness','', 'The coordinator scenario targets 140 users, unlike the separate 75-user manager scenario. Final active users 138 / 140 = **98.57%**, consistent with the rounded 98.6% adoption value. The 98.2% UAT rate over 228 executed cases does not establish exact integer pass counts from the rounded percentage alone. Preserve it as a reported scenario rate until case-level outcomes are supplied. Week 1 UAT and migration have zero activity and should be interpreted as not measured.','', 'Reserve rows are not included in the base-budget totals above. Favorable variance is not an approved reserve transfer.']
    out=ROOT/'verification/SOURCE_RECONCILIATION.md'
    out.write_text('\n'.join(lines)+'\n')
    print(out.relative_to(ROOT))

if __name__=='__main__':main()
