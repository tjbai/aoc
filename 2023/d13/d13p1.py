#!/usr/local/bin/python3

import os
import sys
import logging
from typing import List

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

if len(sys.argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

def sym(g: List[str], i: int) -> bool: 
    for r in range(len(g)):
        check = g[r][:i][::-1]
        logger.debug(f'comparing {check} to {g[r][i:i+len(check)]} at r={r}')
        for a, b in zip(check, g[r][i:i+len(check)]):
            if a != b: return False
    return True

def solve(p: str) -> int:    
    g = p.split('\n')[:-1]
    for i in range(1, len(g[0])):
        if sym(g, i): return i
        
    g = [''.join(x) for x in zip(*g)] # transpose
    for i in range(1, len(g)):
        if sym(g, i): return i * 100
        
    return 0

tot = 0
for p in s.split('\n\n'):
    tot += solve(p)
    
print(tot)