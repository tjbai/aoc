#!/usr/local/bin/python3

from sys import argv
from tqdm import tqdm

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

# rotate counter-clockwise
def rotate(g):
    return [[g[j][i] for j in range(len(g))] for i in range(len(g[0]))]

def cycle(g) -> int:
        
    def slide(c: int) -> int:
        insert = 0
        res = 0
        for i in range(len(g)):
            if g[i][c] == 'O':
                g[i][c] = '.'
                g[insert][c] = 'O'
                insert += 1
                res += len(g) - insert + 1
            elif g[i][c] == '#':
                insert = i + 1
        return res

    return sum(slide(i) for i in range(len(g[0])))

g = [[c for c in line] for line in s.split()]
history = []

for rem in tqdm(range(int(1e10)-1, -1, -1)):
    res = cycle(g)
    
    if res in history:
        i = history.index(res)
        cycle_len = len(history) - i
        offset = rem % cycle_len
        print(history[i + offset])
        print(history)
        break
        
    history.append(res)
    g = rotate(g)