#!/usr/local/bin/python3

'''
a bit more OOP than normal, but for practice
'''

import logging
from sys import argv
import os
from dataclasses import dataclass, replace, asdict
from typing import List, Dict, Tuple, Deque
from collections import deque

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
    
@dataclass
class FuzzyPart:
    x: Tuple[int, int] = (1, 4000)
    m: Tuple[int, int] = (1, 4000)
    a: Tuple[int, int] = (1, 4000)
    s: Tuple[int, int] = (1, 4000)

    def adjust_ranges(self, s: Step, accept: bool) -> 'FuzzyPart':
        fields = asdict(self)
        l, r = fields[s.field]
        
        if s.comp == '<':
            if accept: fields[s.field] = (l, s.threshold - 1)
            else: fields[s.field] = (s.threshold, r)
        
        elif s.comp == '>':
            if accept: fields[s.field] = (s.threshold + 1, r)
            else: fields[s.field] = (l, s.threshold)
            
        return FuzzyPart(**fields)
    
    def valid_ranges(self) -> bool:
        return self.x[0] <= self.x[1] and \
            self.m[0] <= self.m[1] and \
            self.a[0] <= self.a[1] and \
            self.s[0] <= self.s[1]
            
    def combinations(self) -> bool:
        return (self.x[1] - self.x[0] + 1) * \
            (self.m[1] - self.m[0] + 1) * \
            (self.a[1] - self.a[0] + 1) * \
            (self.s[1] - self.s[0] + 1)
            
    def __repr__(self) -> str:
        return f'{{x={self.x},m={self.m},a={self.a},s={self.s}}}'
    
@dataclass
class Workflow():
    steps: List[Step]
    default: str
    
workflow_lines, part_lines = s.split("\n\n")
workflows: Dict[str, Workflow] = {}

for workflow in workflow_lines.split():
    name, _steps = workflow.split('{')
    *steps, default = _steps[:-1].split(',')
    
    workflows[name] = Workflow(
        steps=[Step(s) for s in steps],
        default=default
    )

res = 0
q: Deque[Tuple[FuzzyPart, str]] = deque()
q.append(( FuzzyPart(), 'in' ))

while q:
    fp, cur = q.popleft()
    
    if cur == 'R': continue
    if not fp.valid_ranges: continue
    if cur == 'A':
        res += fp.combinations()
        continue
    
    workflow = workflows[cur]
    for step in workflow.steps:
        # force accept
        q.append(( fp.adjust_ranges(step, True), step.send_to ))
        
        # force reject
        fp = fp.adjust_ranges(step, False)
        
    q.append(( fp, workflow.default ))
    
print(res)