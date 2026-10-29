#!/usr/bin/env python3
"""Recompute finite teaching packets; no business forecast or optimal strategy claim."""
from pathlib import Path
from itertools import combinations
import json

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'examples/business-architecture/decision-packets.json').read_text())
p = data['quarterly_portfolio']
components = p['components']

def totals(selected):
    if len(selected) != len(set(selected)):
        raise ValueError('Count each selected component once')
    return {unit: sum(components[key][unit] for key in selected) for unit in p['limits']}

def feasible(selected, policy_days):
    selected = set(selected)
    if not set(p['mandatory']) <= selected:
        return False
    if any(not set(components[key]['requires']) <= selected for key in selected):
        return False
    limits = dict(p['limits'], policy_days=policy_days)
    return all(value <= limits[unit] for unit, value in totals(selected).items())

keys = tuple(components)
bundles = [set(c) for n in range(len(keys)+1) for c in combinations(keys, n)]
normal = {''.join(sorted(s)) for s in bundles if feasible(s, 6)}
reduced = {''.join(sorted(s)) for s in bundles if feasible(s, 4)}
assert normal == {'R', 'CR', 'ER', 'CER', 'AER', 'BER'}
assert reduced == {'R', 'CR', 'ER', 'CER'}
assert totals(['R','E','A','B']) == {'cash_usd':36000,'engineering_days':14,'policy_days':7}
assert totals(['R','E','B']) == {'cash_usd':24000,'engineering_days':9,'policy_days':5}
assert totals(['R','E','C']) == {'cash_usd':22000,'engineering_days':9,'policy_days':3}
assert not feasible({'R','A'}, 6)  # Inexpensive totals still miss a prerequisite.
try:
    totals(['R','E','E','A'])
except ValueError:
    pass
else:
    raise AssertionError('Duplicate shared enabler was accepted')
m = data['maintenance_offering']
contributions = [m['annual_fee_usd']-m['scheduled_service_and_admin_usd']-n*m['additional_emergency_visit_usd'] for n in range(3)]
assert contributions == [300,100,-100]
assert not m['other_fixed_overhead_included'] and not m['emergency_probabilities_known']
v = data['value_cross_map']
assert len(v['needed']) == len(v['capabilities']) == 4
assert all(len(row) == len(v['stages']) == 4 for row in v['needed'])
assert [sum(row) for row in v['needed']] == [4,3,1,4]
assert [sum(row[i] for row in v['needed']) for i in range(4)] == [3,3,3,3]
print('PASS: all 32 portfolio subsets checked; 6 initially feasible and 4 after policy reduction; prerequisites and unique shared costs preserved.')
print('PASS: maintenance contributions $300/$100/−$100 before omitted overhead; all 16 proposed capability/stage links checked.')
print('Scope: synthetic arithmetic and relationship consistency; no demand, capacity acceptance, benefits or optimal strategy validated.')
