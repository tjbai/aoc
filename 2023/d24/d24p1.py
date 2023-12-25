#!/usr/local/bin/python3

import os
import sys
import logging
from typing import *
from itertools import combinations

env_log = os.environ.get('LOG')
logging.basicConfig(
    level='DEBUG' if env_log else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s' if env_log == '2' else ''
)

logger = logging.getLogger(__name__)

##################################################

if len(sys.argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

'''
Perhaps you won't have to do anything. How likely are the hailstones to collide 
with each other and smash into tiny ice crystals?

To estimate this, consider only the X and Y axes; ignore the Z axis. Looking 
forward in time, how many of the hailstones' paths will intersect within a 
test area? (The hailstones themselves don't have to collide, just test for 
intersections between the paths they will trace.)

X >= 200000000000000 (2e14)
Y >= 400000000000000 (4e14)

iter between all n^2 hailstone position, velocity pairs
linear equation -> intersection point -> fit bounds
'''

trajectories: List[Tuple[int, int]] = []

l, r = 2e14, 4e14
# l, r = 7, 27

for line in s.split('\n'):
    _pos, _velocity = line.split('@')
    px, py, _ = eval(_pos)
    vx, vy, _ = eval(_velocity)
    
    trajectories.append((vx, vy, px, py))
    
res = 0
for (vx1, vy1, px1, py1), (vx2, vy2, px2, py2) in combinations(trajectories, 2):
    m1, m2 = vy1 / vx1, vy2 / vx2
    b1, b2 = py1 - m1 * px1, py2 - m2 * px2
    
    logger.debug(f'\npx1={px1}, py1={py1}, m1={m1}, b1={b1}')
    logger.debug(f'px2={px2}, py2={py2}, m2={m2}, b2={b2}')
    
    if m1 == m2: continue
    
    x_int = (b2 - b1) / (m1 - m2)
    y_int = m1 * x_int + b1
    
    logger.debug(f'x_int={x_int}, y_int={y_int}')
    
    if not (l <= x_int <= r) or not (l <= y_int < r): continue
    if (x_int - px1) / vx1 < 0 or (x_int - px2) / vx2 < 0: continue
    
    res += 1
    
print(res)