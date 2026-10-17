import copy
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',ROOT/'scripts/validate_portfolio.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

class Controls(unittest.TestCase):
    def setUp(self):
        self.data=v.load_case(next(ROOT.glob('*/Control_Exercise')))
    def test_expected_schedule_and_budget(self):
        r=v.evaluate(self.data)
        self.assertEqual(r['errors'],[])
        self.assertEqual(r['finish'],11)
        self.assertEqual(r['schedule']['T-02']['float'],1)
        self.assertEqual(r['forecast'],7100)
        self.assertEqual(r['variance'],-100)
        self.assertEqual(r['gate'],'HOLD')
    def test_schedule_slip_propagates(self):
        self.data['tasks'][2]['duration_days']='7'
        self.assertEqual(v.evaluate(self.data)['finish'],14)
    def test_cycle_fails(self):
        self.data['tasks'][0]['predecessors']='T-06'
        self.assertTrue(v.evaluate(self.data)['errors'])
    def test_orphan_fails(self):
        self.data['tests'][0]['requirement_id']='MISSING'
        self.assertTrue(v.evaluate(self.data)['errors'])
    def test_pass_requires_evidence(self):
        self.data['tests'][0]['evidence']=''
        self.assertTrue(v.evaluate(self.data)['errors'])
    def test_missing_owner_fails(self):
        self.data['actions'][0]['owner']=''
        self.assertTrue(v.evaluate(self.data)['errors'])
    def test_unapproved_change_fails(self):
        self.data['budget'][0]['approved_change_usd']='100'
        self.data['budget'][0]['change_reference']='DEC-01'
        self.assertTrue(v.evaluate(self.data)['errors'])
    def ready_data(self):
        for t in self.data['tasks']:t.update(status='Complete',evidence='SIM-EV-01')
        for t in self.data['tests']:t.update(result='Pass',evidence='SIM-EV-01',observed_result='Synthetic test fixture only')
        for i in self.data['issues']:i.update(status='Closed',closure_evidence='SIM-EV-01')
        for a in self.data['actions']:a.update(status='Complete',closure_evidence='SIM-EV-01')
        for d in self.data['decisions']:d.update(status='Approved',decision_day='11')
        for g in self.data['gates']:g.update(approval='Approved',approval_day='11')
        self.data['budget'][2]['etc_usd']='1200'
    def test_complete_fixture_can_be_ready(self):
        self.ready_data();self.assertEqual(v.evaluate(self.data)['gate'],'READY')
    def test_missing_gate_date_blocks(self):
        self.ready_data();self.data['gates'][0]['approval_day']=''
        self.assertEqual(v.evaluate(self.data)['gate'],'HOLD')
    def test_open_critical_issue_blocks(self):
        self.ready_data();self.data['issues'][0].update(status='Open',severity='Critical')
        self.assertEqual(v.evaluate(self.data)['gate'],'HOLD')
    def test_failed_test_blocks(self):
        self.ready_data();self.data['tests'][4]['result']='Fail'
        self.assertEqual(v.evaluate(self.data)['gate'],'HOLD')
    def test_over_budget_blocks(self):
        self.ready_data();self.data['budget'][2]['etc_usd']='9999'
        self.assertEqual(v.evaluate(self.data)['gate'],'HOLD')
    def test_all_projects_have_valid_records(self):
        for p in ROOT.glob('*/Control_Exercise'):
            with self.subTest(project=p.parent.name):self.assertEqual(v.evaluate(v.load_case(p))['errors'],[])

if __name__=='__main__':unittest.main()
