#!/usr/local/bin/python3

from sys import argv

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

res = 0

def dfs(springs, groups, i, j, cur_group):
    if i == len(springs) and j == len(groups): res += 1
    
    if springs[i] == '#':
        if j == len(groups) or cur_group + 1 > groups[j]: return
        elif cur_group + 1 < groups[j]: dfs(springs, groups, i+1, j, cur_group + 1)
        else: dfs(springs, groups, i+1, j+1, 0)
    
    if springs[i] == '.':
        if cur_group == 0: dfs(springs, groups, i+1, j, 0)
        elif j == len(groups) or cur_group != groups[j]: return
        else: dfs(springs, groups, i+1, j+1, 0)
        
    else:
        


for line in s.split('\n'):
    springs, _groups = line.split()
    groups = list(map(int, _groups.split(',')))
    dfs(springs, groups, 0, 0, 0)