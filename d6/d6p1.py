#!/usr/bin/python3

from math import sqrt, ceil, floor

with open('d6.in') as f:
    s = f.read()
    
_times, _distances = s.split('\n')
times = list(map(int, _times.split(':')[-1].split()))
distances = list(map(int, _distances.split(':')[-1].split()))

# d = x * (t - x)
# x(t - x) >= d
# tx - x^2 >= d
# x^2 - tx + d <= 0
# x = (t +- sqrt(t^2 - 4d)) / 2

res = 1
for t, d in zip(times, distances):
    det = sqrt(t**2 - 4*d)
    lower = ceil((t - det) / 2)
    upper = floor((t + det) / 2)
    
    ways = upper - lower + 1
    if upper**2 - t*upper + d == 0: ways -= 1
    if lower**2 - t*lower + d == 0: ways -= 1

    res *= ways

print(res)