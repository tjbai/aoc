#!/usr/local/bin/python3

import os
import sys
import logging
from collections import defaultdict

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

if len(sys.argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

##################################################

g = s.split('\n')
M, N = len(g), len(g[0])
dirs = {'v': [(1,0)], '>': [(0,1)]}
prune = defaultdict(lambda: -1)

sys.setrecursionlimit(M*N)

def dfs(r: int, c: int, d: int, seen: set) -> int:
    if r < 0 or c < 0 or r == M or c == N: return
    if (r, c) in seen: return
    if d < prune[(r, c)]: return
    if g[r][c] == '#': return    
    
    seen.add((r, c))
    prune[(r, c)] = d
    
    for dr, dc in dirs.get(g[r][c], [(1,0),(-1,0),(0,1),(0,-1)]):
        dfs(r+dr, c+dc, d+1, seen)

    seen.remove((r, c))

dfs(0, 1, 0, set())
print(prune[(M-1, N-2)])