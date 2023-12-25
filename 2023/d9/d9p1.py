#!/usr/local/bin/python3

from sys import argv
from typing import List

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

def solve(nums: List[int]) -> int:
    prev = nums
    res = nums[-1]
    while not all(p == 0 for p in prev): 
        cur = []
        for a, b in zip(prev[:-1], prev[1:]): cur.append(b - a)
        res += cur[-1]
        prev = cur
    return res

print(sum(solve(list(map(int, line.split()))) for line in s.split('\n')))