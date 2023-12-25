#!/usr/local/bin/python3

from sys import argv
from collections import deque

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

g = s.split('\n')

M, N = len(g), len(g[0])
expanded_rows = set(i for i in range(M))
expanded_cols = set(i for i in range(N))

for r in range(M):
    for c in range(N):
        if g[r][c] == '#':
            if r in expanded_rows: expanded_rows.remove(r)
            if c in expanded_cols: expanded_cols.remove(c)
            
def bfs(r: int, c: int) -> int:
    q = deque([(r, c, 0)])
    seen = set()
    ds = dict()
    
    while q:
        r, c, d = q.popleft()
        if (r, c) in seen: continue
        seen.add((r, c))
        
        if r < 0 or c < 0 or r >= M or c >= N: continue
        if g[r][c] == '#': ds[(r, c)] = d
        
        er = 1 if r in expanded_rows else 0
        ec = 1 if c in expanded_cols else 0
        q.append((r+1, c, d+1+er))
        q.append((r-1, c, d+1+er))
        q.append((r, c+1, d+1+ec))
        q.append((r, c-1, d+1+ec))
        
    return ds

res = 0
for r in range(M):
    for c in range(N):
        if g[r][c] == '#':
            res += sum(v for v in bfs(r, c).values())

print(res // 2)