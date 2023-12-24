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

g = s.split('\n')
M, N = len(g), len(g[0])
sys.setrecursionlimit(1000)


def in_bounds(r: int, c: int) -> int:
    return 0 <= r < M and 0 <= c < N and g[r][c] != '#'

def is_intersection(r: int, c: int, dr: int, dc: int) -> int:
    open_slots = 0
    for ddr, ddc in [(-1,-1),(-1,0),(0,-1),(1,1),(0,1),(1,0),(-1,1),(-1,1)]:
        if (dr, dc) == (ddr, ddc) or (-dr, -dc) == (ddr, ddc): continue
        if not in_bounds(r+ddr, c+ddc): continue
        open_slots += 1 if g[r+ddr][c+ddc] != '#' else 0
    return open_slots > 0

contracted = defaultdict(set)
def contract(r: int, c: int, seen: set) -> int:
    if (r,c) in seen: return 
    seen.add((r,c))
    
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        cr, cc = r, c
        d = 0
        while in_bounds(cr+dr, cc+dc):
            d += 1
            cr, cc = cr+dr, cc+dc

            # branch off in new directions
            if is_intersection(r, c, dr, dc):
                contracted[(r,c)].add((cr,cc,d))
                contract(cr, cc, seen)
                
        # always contract at the end of a hall
        if d > 0:
            contracted[(r,c)].add((cr,cc,d))
            contract(cr, cc, seen)
            
contract(0, 1, set())

max_d = defaultdict(int)
def dfs(r: int, c: int, d: int, seen: set) -> int:
    logger.debug(f'r={r} c={c} d={d}')
    if (r, c) in seen: return
    seen.add((r, c))
    
    max_d[(r,c)] = max(max_d[(r,c)], d)
    for nr, nc, dd in contracted[(r,c)]:
        dfs(nr, nc, d+dd, seen)
    
    seen.remove((r, c))

dfs(0, 1, 0, set())
print(max_d[(M-1, N-2)])