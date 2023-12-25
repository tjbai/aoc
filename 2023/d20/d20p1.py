#!/usr/local/bin/python3

# NOTE: lots of OOP for practice

import os
import sys
import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from typing import List, Literal, Dict, Deque, Tuple

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

if len(sys.argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

Pulse = Literal['low', 'high']

@dataclass
class Action:
    sender: str
    receiver: str
    pulse: Pulse
    
    def __repr__(self) -> str:
        return f'{self.sender} -{self.pulse}-> {self.receiver}'

class Module(ABC):
    def __init__(self, name, children):
        self.name = name
        self.children = children
        
    @abstractmethod
    def receive_pulse(self, action: Action) -> List[Action]:
        raise NotImplementedError()
    
    def __repr__(self) -> str:
        return f'{{{self.name} -> {self.children}}}'
    
class Flip(Module):
    def __init__(self, name, children):
        super().__init__(name, children)
        self.on = False
    
    def receive_pulse(self, action: Action) -> List[Action]:
        if action.pulse == 'high': return []

        if self.on:
            self.on = False 
            return [Action(self.name, child, 'low') for child in self.children]
        
        else:
            self.on = True
            return [Action(self.name, child, 'high') for child in self.children]
    
class Conjunction(Module):
    def __init__(self, name, children):
        super().__init__(name, children)
        self.parent_level = defaultdict(lambda: 'low')
    
    @property
    def all_inputs_high(self) -> bool:
        return all(self.parent_level[p] == 'high' for p in parents[self.name])
    
    def receive_pulse(self, action: Action) -> List[Action]:
        self.parent_level[action.sender] = action.pulse
        return [Action(self.name, child, 'low' if self.all_inputs_high else 'high') for child in self.children]

class Broadercaster(Module):
    def receive_pulse(self, action: Action) -> List[Action]:
        return [Action(self.name, child, action.pulse) for child in self.children]

modules: Dict[str, Module] = {}
parents: Dict[str, List[str]] = defaultdict(list)

for line in s.split('\n'):
    parent, _children = line.split(' -> ')
    children = _children.split(', ')
    
    if parent[0] == '%':
        parent = parent[1:]
        modules[parent] = Flip(parent, children)
    elif parent[0] == '&':
        parent = parent[1:]
        modules[parent] = Conjunction(parent, children)
    else:  modules[parent] = Broadercaster(parent, children)
    
    for child in children: parents[child].append(parent)

def bfs() -> Tuple[int, int]:
    low = high = 0
    q: Deque[Action] = deque()
    q.append(Action('button', 'broadcaster', 'low'))
    
    while q:
        cur = q.popleft()
        logging.debug(cur)
        if cur.pulse == 'low': low += 1
        else: high += 1
        if cur.receiver not in modules: continue
        recv_module = modules[cur.receiver]
        q.extend(recv_module.receive_pulse(cur))
        
    return low, high

low = high = 0
for _ in range(1000):
    dlow, dhigh = bfs()
    low += dlow
    high += dhigh
    
print(low * high)