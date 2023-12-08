#!/usr/bin/python3

from sys import argv

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
    
cur = 'AAA'
offset = 0
steps = 0
while cur != 'ZZZ':
    i = 0 if ins[offset] == 'L' else 1
    cur = g[cur][i]
    steps += 1
    offset += 1
    if offset == len(ins): offset = 0
    
print(steps)