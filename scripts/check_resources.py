#!/usr/bin/env python3
"""Offline checks for fictional companion packets; no live service actions."""
from pathlib import Path
import csv,json,math
root=Path(__file__).resolve().parents[1]
for name in ['capabilities','strategy','investment','dependencies']:
 folder=root/'business-practice'/name
 for filename in ['README.md','worksheet.csv','worked-answer.md']:
  assert (folder/filename).is_file(),(name,filename)
 with (folder/'worksheet.csv').open(newline='') as f: rows=list(csv.reader(f))
 assert len(rows)>=2 and len(rows[0])==len(set(rows[0]))
 assert all(len(row)==len(rows[0]) for row in rows)
 assert 'fictional' in (folder/'worked-answer.md').read_text().lower() or 'invented' in (folder/'worked-answer.md').read_text().lower()
assert 8/10==.8 and 2/4==.5
assert 9/12==.75 and math.isclose(4/6,2/3)
d=json.loads((root/'business-practice/investment/synthetic-cost-model.json').read_text())
years=d['horizon_years']; assert years==2
assert d['minimum_repair']['setup_usd']+years*d['minimum_repair']['annual_upkeep_usd']==18000
assert d['conditional_ai_add_on']['setup_usd']+years*d['conditional_ai_add_on']['annual_operation_usd']==40000
assert d['hypothetical_purchase']['r7_fit'] is False
for review in d['review_minutes']:
 values=[d['eligible_questions']*a*(d['baseline_minutes_per_question']-review)/60*d['capacity_value_usd_per_hour'] for a in d['adoption_rates']]
 assert all(math.isclose(a,b,rel_tol=1e-12) for a,b in zip(values,d['chart_capacity_equivalent_usd'][f'review_{review}']))
p=d['paper_exercise']
assert p['smaller_setup_usd']+years*p['smaller_annual_usd']==10000
assert p['aid_setup_usd']+years*p['aid_annual_usd']==18000
hours=[p['eligible_questions']*a*(p['baseline_minutes']-p['review_minutes'])/60 for a in p['adoption_rates']]
assert hours==[150,225]
assert [h*p['capacity_value_usd_per_hour'] for h in hours]==[6000,9000]
for path in (root/'examples').glob('*.csv'):
 with path.open(newline='') as f:rows=list(csv.reader(f))
 assert rows and all(len(row)==len(rows[0]) for row in rows),path.name
print('PASS: four self-study kits, template CSV shape, synthetic costs/sensitivity and existing CSV fixtures.')
print('Scope: offline file/arithmetic checks; no live system, business result or learner validation.')
