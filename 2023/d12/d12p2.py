#!/usr/local/bin/python3

from functools import cache
from sys import argv

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

@cache
def dfs(springs, groups) -> int:
    if not springs: return 0 if groups else 1
    if not groups: return 0 if '#' in springs else 1

    tot = 0

    if springs[0] in '.?':
        tot += dfs(springs[1:], groups)
    
    if springs[0] in '#?':
        if (
            groups[0] <= len(springs) and 
            '.' not in springs[:groups[0]] and 
            (groups[0] == len(springs) or springs[groups[0]] != '#')
        ):
            tot += dfs(springs[groups[0]+1:], groups[1:])
            
    return tot

res = 0    
for line in s.split('\n'):
    _springs, _groups = line.split()
    springs = tuple('?'.join([_springs] * 5))
    groups = tuple(map(int, _groups.split(','))) * 5
    res += dfs(springs, groups)

print(res)