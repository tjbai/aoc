#!/usr/local/bin/python3

from sys import argv
from collections import defaultdict
from heapq import heappush, heappop

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

g = [[int(c) for c in line] for line in s.split()]
M, N = len(g), len(g[0])

nodes = [(0, 0, 0, 1, 0, 1), (0, 0, 0, 0, 1, 1)]
min_d = defaultdict(lambda: float('inf'))
seen = set()

# a node is represented by (d, r, c, dr, dc, n)
while nodes:
    d, r, c, dr, dc, n = heappop(nodes)
    if n > 3: continue
    if (r, c, dr, dc, n) in seen: continue
    seen.add((r, c, dr, dc, n))

    min_d[(r, c)] = min(min_d[(r, c)], d)
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if (dr, dc) == (1, 0): dirs.remove((-1, 0))
    if (dr, dc) == (-1, 0): dirs.remove((1, 0))
    if (dr, dc) == (0, 1): dirs.remove((0, -1))
    if (dr, dc) == (0, -1): dirs.remove((0, 1))
    
    for ddr, ddc, in dirs:
        nr, nc = r+ddr, c+ddc
        if nr < 0 or nc < 0 or nr == M or nc == N: continue
        heappush(nodes, (d+g[nr][nc], r+ddr, c+ddc, ddr, ddc, n+1 if (ddr, ddc) == (dr, dc) else 1))
        
print(min_d[(M-1, N-1)])