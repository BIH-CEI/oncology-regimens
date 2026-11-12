#!/usr/bin/env python3
"""Print a cross-version skeleton for one resource type: which element paths
exist in both FHIR R4 and R6 with the same types (safe to copy), and which
differ (need a hand-written rule). Helper for authoring maps/xver/*.fml.

Usage: skeleton.py <R4 package dir> <R6 package tgz> <ResourceType> [max depth]
"""
import json, sys, tarfile, os

def load_r4(pkgdir, name):
    return json.load(open(os.path.join(pkgdir, f'StructureDefinition-{name}.json')))

def load_r6(tgz, name):
    return json.load(tgz.extractfile(f'package/StructureDefinition-{name}.json'))

BASE = {'id', 'meta', 'implicitRules', 'language', 'text', 'contained', 'extension', 'modifierExtension'}

def elements(sd, depth):
    out = {}
    for e in sd['snapshot']['element']:
        p = e['path']
        parts = p.split('.')
        if len(parts) == 1 or (len(parts) == 2 and parts[1] in BASE):
            continue
        if depth and len(parts) > depth:
            continue
        types = []
        for t in e.get('type', []):
            tp = t['code']
            if t.get('targetProfile'):
                tp += '(' + '|'.join(x.split('/')[-1] for x in t['targetProfile']) + ')'
            types.append(tp)
        if 'contentReference' in e:
            types = ['->' + e['contentReference'].split('#')[-1]]
        out[p] = (f"{e.get('min')}..{e.get('max')}", ','.join(types))
    return out

def main():
    pkgdir, tgzpath, name = sys.argv[1], sys.argv[2], sys.argv[3]
    depth = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    tgz = tarfile.open(tgzpath)
    r4 = elements(load_r4(pkgdir, name), depth)
    r6 = elements(load_r6(tgz, name), depth)
    print(f"== {name}: same path and types (copy) ==")
    for p in r4:
        if p in r6 and r4[p][1] == r6[p][1]:
            card = '' if r4[p][0] == r6[p][0] else f"   # cardinality {r4[p][0]} -> {r6[p][0]}"
            print(f"  {p}{card}")
    print(f"== {name}: in both, types differ ==")
    for p in r4:
        if p in r6 and r4[p][1] != r6[p][1]:
            print(f"  {p}: R4 {r4[p][0]} {r4[p][1]}  ->  R6 {r6[p][0]} {r6[p][1]}")
    print(f"== {name}: R4 only ==")
    for p in r4:
        if p not in r6:
            print(f"  {p} {r4[p][0]} {r4[p][1]}")
    print(f"== {name}: R6 only ==")
    for p in r6:
        if p not in r4:
            print(f"  {p} {r6[p][0]} {r6[p][1]}")

if __name__ == '__main__':
    main()
