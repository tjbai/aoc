#!/usr/local/bin/python3

'''
a bit more OOP than normal, but for practice
'''

import logging
from sys import argv
import os
from dataclasses import dataclass
from typing import List, Dict

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 
    
@dataclass
class Part():
    x: int
    m: int
    a: int
    s: int
    
    def __init__(self, s: str):
        _fields = s[1:-1].split(',')
        self.x, self.m, self.a, self.s = list(map(int, (int(f.split('=')[1]) for f in _fields)))
    
    def rating(self) -> int:
        return self.x + self.m + self.a + self.s
    
    def __repr__(self) -> str:
        return f'{{x={self.x},m={self.m},a={self.a},s={self.s}}}'

@dataclass
class Step():
    field: str
    comp: str
    threshold: int
    send_to: str
    
    def __init__(self, s: str):
        self.field = s[0]
        self.comp = s[1]
        _threshold, self.send_to = s[2:].split(':')
        self.threshold = int(_threshold)
        
    def __repr__(self) -> str:
        return f'{self.field}{self.comp}{self.threshold}:{self.send_to}'
        
    def check(self, p: Part) -> bool:
        part_fields = {'x': p.x, 'm': p.m, 'a': p.a, 's': p.s}
        logger.debug('Comparing {p} with {self}')
        if self.comp == '<' and part_fields[self.field] < self.threshold: return True
        if self.comp == '>' and part_fields[self.field] > self.threshold: return True
        return False
    
@dataclass
class Workflow():
    steps: List[Step]
    default: str
    
    def process(self, p: Part) -> str:
        for s in self.steps:
            if s.check(p): return s.send_to
        return self.default
    
workflow_lines, part_lines = s.split("\n\n")
workflows: Dict[str, Workflow] = {}
parts: List[Part] = [Part(p) for p in part_lines.split()]

for workflow in workflow_lines.split():
    name, _steps = workflow.split('{')
    *steps, default = _steps[:-1].split(',')
    
    workflows[name] = Workflow(
        steps=[Step(s) for s in steps],
        default=default
    )
    
tot = 0
for part in parts:
    cur = 'in'
    while cur not in {'A', 'R'}:
        cur = workflows[cur].process(part)
    if cur == 'A': tot += part.rating()
    
print(tot)