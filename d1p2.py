#!/usr/bin/python3

import fileinput

ds = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def solve(s: str) -> int:
    nums = []
    i = 0
    while i < len(s):
        for ss, val in ds.items():
            if i + len(ss) < len(s) and s[i:i+len(ss)] == ss:
                nums.append(val)
                
        if s[i].isnumeric(): 
            nums.append(int(s[i]))
            
        i += 1

    return nums[0] * 10 + nums[-1]

tot = 0
for line in fileinput.input():
    tot += solve(line)

print(tot)
