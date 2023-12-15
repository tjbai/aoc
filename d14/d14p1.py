#!/usr/local/bin/python3

from sys import argv

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

g = [[c for c in line] for line in s.split()]
M, N = len(g), len(g[0])

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
            
print(sum(slide(i) for i in range(N)))