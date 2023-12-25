#!/usr/local/bin/python3

import os
import sys
import logging
from collections import defaultdict, deque

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

if len(sys.argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

g = defaultdict(list)
for line in s.split('\n'):
    l, _right = line.split(':')
    right = _right.strip().split(' ')
    for r in right:
        g[l].append(r)
        g[r].append(l)
        
# print(sum(len(v) for v in g.values())) # 66/6900 total edges
# print(len(g)) # 15/1539 total nodes

# 6900 C 3
# 7000 C 2, DFS for one cut point?

def inc(a: str, b: str, s: set):
    if a < b: s[(a,b)] += 1
    else: s[(b,a)] += 1
    
edge_ct = defaultdict(int)
def bfs(n: str):
    seen = set()
    q = deque([(n, '')])
    while q:
        cur, par = q.popleft()
        if cur in seen: continue
        seen.add(cur)
        inc(cur, par, edge_ct)
        for n in g[cur]: q.append((n, cur))
        
for n in g: bfs(n)

# inspection: (jll, lnf), (cmj, qhd), (kkp, vtv)
# print(sorted(edge_ct.items(), key=lambda x: x[1], reverse=True)[:10])

seen = set()
q = deque(['jll'])
restricted = {
    ('jll', 'lnf'), ('cmj', 'qhd'), ('kkp', 'vtv'),
    ('lnf', 'jll'), ('qhd', 'cmj'), ('vtv', 'kkp')
}

sz = 0
while q:
    cur = q.popleft()
    if cur in seen: continue
    seen.add(cur)
    sz += 1
    for n in g[cur]:
        if (cur, n) in restricted: continue
        q.append(n)
        
print(sz, len(g) - sz) # 785, 754