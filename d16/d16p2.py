#!/usr/local/bin/python3

from sys import argv
from collections import deque
from time import sleep

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

g = [[c for c in line] for line in s.split()]
M, N = len(g), len(g[0])

def solve(sr, sc, dr, dc):
    seen = set()
    energized = set()
    q = deque([(sr, sc, dr, dc)])

    while q:
        r, c, dr, dc = q.popleft()
        if not (0 <= r < M and 0 <= c < N): continue
        if (r, c, dr, dc) in seen: continue
        
        seen.add((r, c, dr, dc))
        energized.add((r, c))
        cur = g[r][c]
        
        if cur == '.': q.append((r+dr, c+dc, dr, dc))
        
        elif dc != 0:
            if cur == '-':
                q.append((r+dr, c+dc, dr, dc))
            elif cur == '\\':
                dr, dc = dc, 0
                q.append((r+dr, c+dc, dr, dc))
            elif cur == '/':
                dr, dc = -dc, 0
                q.append((r+dr, c+dc, dr, dc))
            elif cur == '|':
                q.append((r+1, c, 1, 0))
                q.append((r-1, c, -1, 0))
        
        elif dr != 0:
            if cur == '|': q.append((r+dr, c+dc, dr, dc))
            elif cur == '\\':
                dc, dr = dr, 0
                q.append((r+dr, c+dc, dr, dc))
            elif cur == '/':
                dc, dr = -dr, 0
                q.append((r+dr, c+dc, dr, dc))
            elif cur == '-':
                q.append((r, c+1, 0, 1))
                q.append((r, c-1, 0, -1))
                
    return len(energized)
    
res = 0

# every starting left and right
for i in range(M):
    res = max(res, solve(i, 0, 0, 1))
    res = max(res, solve(i, N-1, 0, -1))

# every starting up and down
for i in range(N):
    res = max(res, solve(0, i, 1, 0))
    res = max(res, solve(M-1, i, -1, 0))
    
print(res)