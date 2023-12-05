#!/usr/bin/python3

import fileinput

def solve(s: str) -> int:
    nums = [int(c) for c in s if c.isnumeric()]
    return nums[0] * 10 + nums[-1]

tot = 0
for line in fileinput.input():
    tot += solve(line)

print(tot)