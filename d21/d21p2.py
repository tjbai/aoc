#!/usr/local/bin/python3

import os
import sys
import logging
from collections import deque
from tqdm import tqdm

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

if len(sys.argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

g = [[c for c in line] for line in s.split('\n')]
M, N = len(g), len(g[0])
q = deque()

for r in range(M):
    for c in range(N):
        if g[r][c] == 'S':
           q.append((r, c)) 
           break
    
# track offsets for positions, but also unique coordinates   
for _ in tqdm(range(26501365)):
    sz = len(q)
    seen = set()
    for _ in range(sz):
        r, c = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            rr, rc = nr % M, nc % N
            if g[rr][rc] == '#' or (nr, nc) in seen: continue
            seen.add((nr, nc))
            q.append((nr, nc))
            
print(len(q))