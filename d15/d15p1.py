#!/usr/local/bin/python3

from sys import argv

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 
        
def solve(s: str) -> int:
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res

print(sum(solve(sub) for sub in s.split(',')))