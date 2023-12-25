#!/usr/local/bin/python3

import os
import sys
import logging

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

if len(sys.argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

'''
now considering all coordinates find a starting position, velocity pair
that will allow us to hit ALL hailstones at some point in the future

idea (with hint):
p(t) = v * t + p_0

for each (v_i, p_0i) we need v * t + p_0 = v_i * t + p_0i
=> (v - v_i) * t + (p_0 - p_0i) = 0
'''