#!/usr/bin/python3

with open('d3.txt') as f:
    s = f.read()

grid = s.split('\n')

M, N = len(grid), len(grid[0])
dirs = [(-1,-1),(-1,0),(0,-1),(1,1),(1,0),(0,1),(1,-1),(-1,1)]

def is_adj(r, ind) -> bool:
    for c in ind:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= M or nc >= N: continue
            if not grid[nr][nc].isdigit() and grid[nr][nc] != '.': return True
    return False

tot = 0
for r in range(M):
    num = ''
    ind = []
    for c in range(N):
        if grid[r][c].isdigit():
            num += grid[r][c]
            ind.append(c)
        else:
            tot += int(num) if is_adj(r, ind) else 0
            num = ''
            ind = []
    tot += int(num) if is_adj(r, ind) else 0

print(tot)