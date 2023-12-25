#!/usr/local/bin/python3

from sys import argv

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

def dfs(springs, groups, i) -> int:
    if i == len(springs):
        joined_springs = list(filter(len, ''.join(springs).split('.')))
        if len(joined_springs) != len(groups): return 0
        return all(len(x) == groups[i] for i, x in enumerate(joined_springs))
    
    if springs[i] == '?':
        tot = 0
        springs[i] = '.'
        tot += dfs(springs, groups, i+1)
        springs[i] = '#'
        tot += dfs(springs, groups, i+1)
        springs[i] = '?'
        return tot
    
    return dfs(springs, groups, i+1)

res = 0    
for line in s.split('\n'):
    _springs, _groups = line.split()
    springs = list(_springs)
    groups = list(map(int, _groups.split(',')))
    res += dfs(springs, groups, 0)

print(res)