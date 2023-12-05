#!/usr/bin/python3

from collections import defaultdict
from bisect import bisect_left

with open('d5.in') as f:
    s = f.read()
    
chunks = s.split('\n\n')
_seeds = chunks[0].split(':')[-1].strip().split()
seeds = list(map(int, _seeds))

mapping = {}
ranges = defaultdict(list)
range_ends = defaultdict(list)

for ch in chunks[1:]:
    for i, line in enumerate(ch.split('\n')):
        if i == 0:
            s = line.split()[0].split('-')
            sp, dp = s[0], s[-1]
            mapping[sp] = dp
        else:
            ds, ss, l = list(map(int, line.split()))
            ranges[sp].append((ss, ss+l-1, ds-ss))
            range_ends[sp].append(ss+l-1)
            
ranges = {k: sorted(v, key=lambda x: x[1]) for k, v in ranges.items()}
range_ends = {k: sorted(v) for k, v in range_ends.items()}

def get_mapping(source: str, n: int) -> tuple:
    dest = mapping[source]
    i = bisect_left(range_ends[source], n)
    if i >= len(ranges[source]): return (dest, n)
    if n < ranges[source][i][0]: return (dest, n)
    return (dest, n + ranges[source][i][2])
    
def traverse(source: str, n: int) -> int:
    while source != 'location': source, n = get_mapping(source, n)
    return n

res = float('inf')
for i in range(0, len(seeds), 2):
    l, r = seeds[i], seeds[i+1]
    for i in range(r): res = min(res, traverse('seed', l+i))
   
print(res)