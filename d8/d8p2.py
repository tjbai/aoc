#!/usr/bin/python3

from sys import argv
import numpy as np # cheating?

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

ins = None
g = {}
cur = []
for line in s.split('\n'):
    if not line: continue
    if ins is None:
        ins = line
        continue
    node, left, right = line[0:3], line[7:10], line[12:15]
    g[node] = left, right 
    if node[-1] == 'A': cur.append(node)
    
def period(node: str) -> int:
    offset = 0
    steps = 0
    while node[-1] != 'Z':
        i = 0 if ins[offset] == 'L' else 1
        node = g[node][i]
        steps += 1
        offset += 1
        if offset == len(ins): offset = 0
    return steps
    
# too slow :/
def lcm(nums, incs) -> int:
    while not all(n == nums[0] for n in nums):
        i = nums.index(min(nums))
        nums[i] += incs[i]
    return nums[0]
    
ps = [period(n) for n in cur]
print(np.lcm.reduce(ps))