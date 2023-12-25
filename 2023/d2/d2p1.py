#!/usr/bin/python3

import fileinput 

contains = {'red': 12, 'green': 13, 'blue': 14}

def solve(s: str) -> int:
    _id, _sets = s.split(':')
    id = int(_id.split()[-1])
    sets = _sets.strip().split(';')
    
    for set in sets:
        for cubes in set.split(','):
            _ct, color = cubes.strip().split()
            ct = int(_ct)
            if ct > contains[color]:
                return 0
            
    return id

tot = 0
for line in fileinput.input():
    tot += solve(line)

print(tot)