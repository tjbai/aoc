#!/usr/local/bin/python3

from sys import argv

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

dirs = {
    '|': [(0,-1),(0,1)],
    '-': [(-1,0),(1,0)],
    'L': [(0,-1),(1,0)],
    'J': [(0,1),(1,0)],
    '7': [(-1,0),(0,1)],
    'F': [(-1,0),(0,-1)],
    '.': [],
    'S': []
}

grid = [[c for c in line] for line in s.split('\n')]
M, N = len(grid), len(grid[0])
seen = set()

def dfs(r, c, pr, pc) -> bool:
    if r < 0 or c < 0 or r >= M or c >= N: return False
    if (r, c) in seen: return True
    seen.add((r, c))
    
    if grid[r][c] not in {'.', 'O', 'I'}:
        is_border = False
        for dr, dc in dirs[grid[r][c]]: is_border |= r+dr == pr and c+dc == c
        return is_border

    aa, ab, ac, ad = dfs(r+1, c, r, c) , dfs(r-1, c, r, c) , dfs(r, c+1, r, c) , dfs(r, c-1, r, c)
    print(r, c, aa, ab, ac, ad)
    return True
    # grid[r][c] = 'I' if valid else 'O'
    # return valid

for r in range(M):
    for c in range(N):
        if grid[r][c] == '.': dfs(r, c, r, c)

for row in grid:
    print(' '.join(row))