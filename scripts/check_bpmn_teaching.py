#!/usr/bin/env python3
"""Check this teaching subset's graph invariants, not full BPMN conformance."""
from pathlib import Path
import xml.etree.ElementTree as E
ROOT = Path(__file__).resolve().parents[1]
NS = {'b': 'http://www.omg.org/spec/BPMN/20100524/MODEL', 'd': 'http://www.omg.org/spec/BPMN/20100524/DI'}

def inspect(path):
    root = E.parse(path).getroot()
    nodes = {n.get('id'): n for n in root.iter() if n.get('id')}
    if len(nodes) != sum(bool(n.get('id')) for n in root.iter()):
        raise ValueError('Duplicate model IDs')
    owner = {}
    for process in root.findall('b:process', NS):
        assert process.get('isExecutable') == 'false', 'Teaching model must remain non-executable'
        for node in process:
            if node.get('id'):
                owner[node.get('id')] = process.get('id')
    issues = []
    for flow in root.findall('.//b:sequenceFlow', NS):
        source, target = flow.get('sourceRef'), flow.get('targetRef')
        assert source in nodes and target in nodes
        if owner.get(source) != owner.get(target):
            issues.append('cross-participant sequence flow: ' + flow.get('id'))
    for flow in root.findall('.//b:messageFlow', NS):
        source, target = flow.get('sourceRef'), flow.get('targetRef')
        assert source in nodes and target in nodes
        if owner.get(source) == owner.get(target):
            issues.append('same-participant message flow: ' + flow.get('id'))
    for gateway in root.findall('.//b:exclusiveGateway', NS):
        outgoing = [f for f in root.findall('.//b:sequenceFlow', NS) if f.get('sourceRef') == gateway.get('id')]
        assert len(outgoing) == 2
        assert gateway.get('default') in [f.get('id') for f in outgoing]
        for flow in outgoing:
            if flow.get('id') != gateway.get('default'):
                assert flow.find('b:conditionExpression', NS) is not None
    for shape in root.findall('.//d:BPMNShape', NS) + root.findall('.//d:BPMNEdge', NS):
        assert shape.get('bpmnElement') in nodes, 'Diagram refers to missing model object'
    return issues

if __name__ == '__main__':
    folder = ROOT / 'examples/formal-methods/bpmn'
    assert inspect(folder / 'r7-staff-handoff.bpmn') == []
    issues = inspect(folder / 'r7-handoff-broken.bpmn')
    assert set(issues) == {'cross-participant sequence flow: Flow_4', 'same-participant message flow: MessageFlow_Request'}
    print('PASS: corrected BPMN graph; broken fixture rejected for both intended boundary defects')
    print('Scope: XML parsing and selected graph/reference invariants; not complete XSD, BPMN conformance, engine or business validation')
