#!/usr/local/bin/python3

from sys import argv
from typing import List

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

def solve(nums: List[int]) -> int:
    prev = nums
    starts = [nums[0]]
    while not all(p == 0 for p in prev): 
        cur = []
        for a, b in zip(prev[:-1], prev[1:]): cur.append(b - a)
        starts.append(cur[0])
        prev = cur

    res = 0
    for s in starts[::-1]: res = s - res
    return res

print(sum(solve(list(map(int, line.split()))) for line in s.split('\n')))