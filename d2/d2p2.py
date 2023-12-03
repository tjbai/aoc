#!/usr/bin/python3

import fileinput 
from collections import defaultdict

def solve(s: str) -> int:
    _, _sets = s.split(':')
    sets = _sets.strip().split(';')
    mn = defaultdict(int)
    
    for set in sets:
        for cubes in set.split(','):
            _ct, color = cubes.strip().split()
            ct = int(_ct)
            mn[color] = max(mn[color], ct)
    
    return mn['red'] * mn['blue'] * mn['green']

tot = 0
for line in fileinput.input():
    tot += solve(line)

print(tot)