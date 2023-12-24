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

def check_vertical(g, i) -> bool: 
    M, N = len(g), len(g[0])
    
    # go across every row
    for r in range(M):
        for c in range(i, -1, -1):
    
    pass
    
def check_horizontal(g, i) -> bool:
    M, N = len(g), len(g[0])
    pass

def solve(p: str) -> int:
    g = [[c for c in line] for line in p.split('\n')]
    M, N = len(g), len(g[0])
    
    for i in range(M-1):
        if check_horizontal(g, i): return 100*(i+1)
        
    for i in range(N-1):
        if check_vertical(g, i): return i+1
    
print(sum(solve(p) for p in s.split('\n\n')))