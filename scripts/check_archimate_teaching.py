#!/usr/bin/env python3
"""Check this bounded teaching graph, not general ArchiMate conformance."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = {
    ('Process', 'Realization', 'Requirement'),
    ('Process', 'Realization', 'Capability'),
    ('Service', 'Serving', 'Process'),
    ('ApplicationComponent', 'Realization', 'Service'),
}

def check(path):
    model = json.loads(path.read_text())
    errors = []
    if model.get('version') != '4':
        errors.append('wrong language version')
    elements = {e['id']: e for e in model['elements']}
    if len(elements) != len(model['elements']):
        errors.append('duplicate element ID')
    for rel in model['relationships']:
        if rel['source'] not in elements or rel['target'] not in elements:
            errors.append('missing relationship endpoint')
            continue
        pair = (elements[rel['source']]['type'], rel['type'], elements[rel['target']]['type'])
        if pair not in PROFILE:
            errors.append('outside selected teaching profile')
    # Domain assertions for this exercise; a general type checker cannot infer them.
    if elements['ability']['name'] != 'Explain current status and next action accurately':
        errors.append('capability replaced by implementation name')
    serving = [r for r in model['relationships'] if r['type'] == 'Serving']
    if len(serving) != 1 or (serving[0]['source'], serving[0]['target']) != ('offering', 'work'):
        errors.append('service must serve explanation process in this case')
    return errors

if __name__ == '__main__':
    folder = ROOT / 'examples/formal-methods/archimate'
    assert not check(folder / 'r7-explanation.json')
    rejected = check(folder / 'r7-explanation-broken.json')
    assert 'capability replaced by implementation name' in rejected
    assert 'service must serve explanation process in this case' in rejected
    print('PASS: selected ArchiMate 4 teaching graph; both intended meaning defects rejected')
    print('Scope: local profile and case expectations; not general conformance or implementation proof')
