#!/usr/bin/python3

from math import sqrt, ceil, floor

with open('d6.in') as f:
    s = f.read()
    
_t, _d = s.split('\n')
t = int(''.join(_t.split(':')[-1].split()))
d = int(''.join(_d.split(':')[-1].split()))

det = sqrt(t**2 - 4*d)
lower = ceil((t - det) / 2)
upper = floor((t + det) / 2)

ways = upper - lower + 1
if upper**2 - t*upper + d == 0: ways -= 1
if lower**2 - t*lower + d == 0: ways -= 1

print(ways)
