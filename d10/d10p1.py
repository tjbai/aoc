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

grid = s.split('\n')
M, N = len(grid), len(grid[0])

into = defaultdict(set)
outo = defaultdict(set)
for r in range(M):
    for c in range(N):
        if grid[r][c] == 'S': sr, sc = r, c
        for dr, dc in dirs[grid[r][c]]:
            into[(r,c)].add((r+dr,c+dc))
            outo[(r,c)].add((r+dr,c+dc))

max_d = 0
outo[(sr,sc)] = {(sr+1,sc),(sr-1,sc),(sr,sc+1),(sr,sc-1)}
q = deque([(sr,sc,0)])
seen = set()

new_grid = [['.' for _ in range(N)] for _ in range(M)]

while q:
    cr,cc,d = q.popleft()
    if (cr,cc) in seen: continue
    seen.add((cr,cc))
    
    max_d = max(max_d, d)
    new_grid[cr][cc] = str(d)

    for nr,nc in outo[(cr,cc)]:
        if (cr,cc) in into[(nr,nc)]:
            q.append((nr,nc,d+1))
            
print(max_d)