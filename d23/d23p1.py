#!/usr/local/bin/python3

import os
import sys
import logging
from collections import deque

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

def dfs(r: int, c: int, seen: set) -> int:
    if r < 0 or c < 0 or r == M or c == N: return 0
    if (r, c) in seen: return 0
    if (r, c) == (M-1, N-2): return 0
    if g[r][c] == '#': return 0
    
    seen.add((r, c))
    res = -1
    for dr, dc in dirs.get(g[r][c], [(1,0),(-1,0),(0,1),(0,-1)]):
        res = max(res, dfs(r+dr, c+dc, seen))

    seen.remove((r, c))
    return 1 + res

print(dfs(0, 1, set()))