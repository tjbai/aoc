#!/usr/local/bin/python3

from sys import argv
from collections import defaultdict
from functools import lru_cache

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

@lru_cache(maxsize=None)
def key(s: str) -> int:
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res

boxes = defaultdict(dict)

def remove(label: s):
    if label in boxes[key(label)]: del boxes[key(label)][label]    

def insert(label: s, focal_length: s):
    boxes[key(label)][label] = int(focal_length)

for sub in s.split(','):
    if '-' in sub: remove(sub[:-1])
    else: insert(*sub.split('='))

res = 0
for box, lenses in boxes.items():
    for i, (_, focal_length) in enumerate(lenses.items()):
        res += (box + 1) * (i + 1) * focal_length
print(res)