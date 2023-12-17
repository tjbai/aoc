#!/usr/local/bin/python3

from sys import argv
from collections import deque
from time import sleep

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

# the beam is in a cycle if it's at the same square with same direction
# the directions are l, r, u, d

g = [[c for c in line] for line in s.split()]
M, N = len(g), len(g[0])

seen = set() # (r, c, dr, dc)
energized = set() # (r, c)
q = deque([(0, 0, 0, 1)])

while q:
    r, c, dr, dc = q.popleft()
    if not (0 <= r < M and 0 <= c < N): continue
    if (r, c, dr, dc) in seen: continue
    
    seen.add((r, c, dr, dc))
    energized.add((r, c))
    cur = g[r][c]
    
    if cur == '.': q.append((r+dr, c+dc, dr, dc))
    
    # going horizontally
    elif dc != 0:
        if cur == '-': # continue like normal
            q.append((r+dr, c+dc, dr, dc))
        elif cur == '\\': # negative swap
            dr, dc = dc, 0
            q.append((r+dr, c+dc, dr, dc))
        elif cur == '/': # positive swap
            dr, dc = -dc, 0
            q.append((r+dr, c+dc, dr, dc))
        elif cur == '|': # split
            q.append((r+1, c, 1, 0))
            q.append((r-1, c, -1, 0))
    
    # going vertically
    elif dr != 0:
        if cur == '|': q.append((r+dr, c+dc, dr, dc))
        elif cur == '\\': # negative swap
            dc, dr = dr, 0
            q.append((r+dr, c+dc, dr, dc))
        elif cur == '/': # positive swap
            dc, dr = -dr, 0
            q.append((r+dr, c+dc, dr, dc))
        elif cur == '-': # split
            q.append((r, c+1, 0, 1))
            q.append((r, c-1, 0, -1))
    
print(len(energized))