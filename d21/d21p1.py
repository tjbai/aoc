#!/usr/local/bin/python3

import os
import sys
import logging
from collections import deque
from time import sleep

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
       
for _ in range(64):
    sz = len(q)
    seen = set()
    for _ in range(sz):
        r, c = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if nr < 0 or nc < 0 or nr == M or nc == N: continue
            if g[nr][nc] == '#' or (nr, nc) in seen: continue
            seen.add((nr, nc))
            q.append((nr, nc))

print(len(q))