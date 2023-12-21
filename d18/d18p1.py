#!/usr/local/bin/python3

from sys import argv
from collections import deque

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f:
    s = f.read() 
    lines = s.split('\n')

lm = ln = um = un = r = c = 0
trench = set([(0, 0)])
dirs = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}

for line in lines:
    d, n = line[0], int(line[2])
    dr, dc = dirs[d]
    
    for _ in range(n):
        r, c = r+dr, c+dc
        trench.add((r, c))
    
    um, un = max(um, r), max(un, c)
    lm, ln = min(lm, r), min(ln, c)
    
M = um - lm + 1
N = un - ln + 1
grid = [['.' for _ in range(N)] for _ in range(M)]
for r, c in trench: grid[r-lm][c-ln] = '#'

def fill(r, c):
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        if r < 0 or r > M or c < 0 or c > N: continue
        if grid[r][c] != '.': continue
        grid[r][c] = '#'
        q.append((r+1, c))
        q.append((r-1, c))
        q.append((r, c+1))
        q.append((r, c-1))
