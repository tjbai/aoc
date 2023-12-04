#!/usr/bin/python3

with open('d4.in') as f:
    s = f.read()
    
tot = 0
for line in s.split('\n'):
    nums = line.split(':')[-1].strip()
    _winning, _mine = nums.split('|')
    winning = set(map(int, _winning.split()))
    mine = set(map(int, _mine.split()))
    tot += (1 << len(winning & mine)) // 2
    
print(tot)