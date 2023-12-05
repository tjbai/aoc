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

def get_mapping(source: str, l: int, r: int) -> tuple:
    cur_ranges = ranges[source]
    dest = mapping[source]
    dest_ranges = []
    
    i = bisect_left(range_ends[source], l)
    if i >= len(cur_ranges) or r < cur_ranges[i][0]:
        return (dest, [(l, r)])
    
    while i < len(cur_ranges) and r >= cur_ranges[i][0] and l < r:
        range_l, range_r, diff = cur_ranges[i]
        if l < range_l:
            dest_ranges.append((l, range_l-1))
            l = range_l
        dest_ranges.append((l+diff, min(r, range_r)+diff))
        l = min(r, range_r) + 1
        i += 1
    
    if l < r: dest_ranges.append((l, r))
    
    return dest, dest_ranges
    
def traverse(source: str, ranges: list) -> int:
    while source != 'location':
        new_ranges = []
        for r in ranges:
            print(source, 'processing', r)
            dest, dest_ranges = get_mapping(source, r[0], r[1])
            new_ranges.extend(dest_ranges)
        source = dest
        ranges = new_ranges[:]

    return min(r[0] for r in ranges)

res = float('inf')
for i in range(0, len(seeds), 2):
    l, r = seeds[i], seeds[i+1]
    res = min(res, traverse('seed', [(l, l+r-1)]))
   
print(res)