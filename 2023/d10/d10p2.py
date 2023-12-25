#!/usr/local/bin/python3

from sys import argv
from collections import defaultdict, deque

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

dirs = {
    '|': [(-1,0),(1,0)],
    '-': [(0,-1),(0,1)],
    'L': [(-1,0),(0,1)],
    'J': [(0,-1),(-1,0)],
    '7': [(0,-1),(1,0)],
    'F': [(0,1),(1,0)],
    '.': [],
    'S': []
}

g = [[c for c in line] for line in s.split('\n')]
M, N = len(g), len(g[0])

into = defaultdict(set)
outo = defaultdict(set)
for r in range(M):
    for c in range(N):
        if g[r][c] == 'S': sr, sc = r, c
        for dr, dc in dirs[g[r][c]]:
            into[(r,c)].add((r+dr,c+dc))
            outo[(r,c)].add((r+dr,c+dc))

outo[(sr,sc)] = {(sr+1,sc),(sr-1,sc),(sr,sc+1),(sr,sc-1)}
q = deque([(sr,sc,0)])
pipe = set()

while q:
    cr, cc, d = q.popleft()
    if (cr, cc) in pipe: continue
    pipe.add((cr, cc))
    for nr,nc in outo[(cr, cc)]:
        if (cr, cc) in into[(nr, nc)]:
            q.append((nr, nc, d+1))
        
def raycast(r: int) -> int:
    res = 0
    inside = False
    for c in range(N):
        # credit to https://github.com/akolybelnikov/advent_of_code_2023/blob/main/src/bin/day10/main.rs
        if (r, c) in pipe and g[r][c] in {'|', 'L', 'J'}: inside = not inside
        elif (r, c) not in pipe and inside: res += 1
    return res

print(sum(raycast(r) for r in range(M)))