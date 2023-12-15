#!/usr/local/bin/python3

from sys import argv
from tqdm import tqdm

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

g = [[c for c in line] for line in s.split()]
M, N = len(g), len(g[0])

# rotate counter-clockwise
def rotate(g):
    return [[g[j][i] for j in range(len(g))] for i in range(len(g[0])-1,-1,-1)]

def cycle(g) -> int:
        
    def slide(c: int) -> int:
        insert = 0
        res = 0
        for i in range(M):
            if g[i][c] == 'O':
                g[i][c] = '.'
                g[insert][c] = 'O'
                insert += 1
                res += M - insert + 1
            elif g[i][c] == '#':
                insert = i + 1
        return res

    return sum(slide(i) for i in range(len(g[0])))

for _ in tqdm(range(int(1e10))):
    res = cycle(g)
    g = rotate(g)
    
res = cycle(g)

print(res)