#!/usr/local/bin/python3

from sys import argv
from collections import deque

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f:
    s = f.read() 
    lines = s.split('\n')

M = N = r = c = 0
trench = set([(0, 0)])
dirs = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}

for line in lines:
    d, n = line[0], int(line[2])
    dr, dc = dirs[d]
    
    for _ in range(n):
        r, c = r+dr, c+dc
        trench.add((r, c))
    
    M, N = max(M, r+1), max(N, c+1)
    
# grid = [['.' for _ in range(N)] for _ in range(M)]
# for r, c in trench:
#     grid[r][c] = '#'
    
# for row in grid:
#     print(row)
    
def fill(r, c) -> int:
    filled = 0
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        if r < 0 or r == M or c < 0 or c == N: continue
        if (r, c) in trench: continue
        trench.add((r, c))
        filled += 1
        q.append((r+1, c))
        q.append((r-1, c))
        q.append((r, c+1))
        q.append((r, c-1))
    return filled

outside = sum(fill(r, 0) + fill(r, N-1) for r in range(M))\
        + sum(fill(0, c) + fill(M-1, c) for c in range(N))
print(M*N-outside)