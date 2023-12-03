#!/usr/bin/python3

with open('d3.txt') as f:
    s = f.read()

grid = list(map(list, s.split('\n')))

M, N = len(grid), len(grid[0])
dirs = [(-1,-1),(-1,0),(0,-1),(1,1),(1,0),(0,1),(1,-1),(-1,1)]
nums = {}
id = 0

for r in range(M):
    num = ''
    ind = []
    for c in range(N+1):
        if c < N and grid[r][c].isdigit():
            num += grid[r][c]
            ind.append(c)
        elif len(num):
            for oc in ind: grid[r][oc] = str(id)
            nums[id] = int(num)
            id += 1
            num = ''
            ind = []
            
tot = 0
for r in range(M):
    for c in range(N):
        if grid[r][c] != '*': continue
        
        adj = set()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc 
            if nr < 0 or nc < 0 or nr >= M or nc >= M: continue
            if grid[nr][nc].isnumeric(): adj.add(int(grid[nr][nc]))
            
        if len(adj) == 2:
            dtot = 1
            for id in adj: dtot *= nums[id]
            tot += dtot
        
print(tot)