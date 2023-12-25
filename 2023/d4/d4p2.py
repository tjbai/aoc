#!/usr/bin/python3

with open('d4.in') as f:
    s = f.read()

lines = s.split('\n')
N = len(lines)
dc = [0 for _ in range(N)]
c = 1

tot = 0
for i, line in enumerate(lines):
    c += dc[i]
    tot += c
    
    nums = line.split(':')[-1].strip()
    _winning, _mine = nums.split('|')
    winning = set(map(int, _winning.split()))
    mine = set(map(int, _mine.split()))
    matches = len(winning & mine)
    
    if i+1 < N: dc[i+1] += c
    if i+matches+1 < N: dc[i+matches+1] -= c

print(tot)