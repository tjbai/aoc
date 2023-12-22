#!/usr/local/bin/python3

# NOTE: lots of OOP for practice

import os
import sys
import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from typing import List, Literal, Dict, Deque

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
notes:
- pulses are processed in bfs
- %
    - high pulse, ignore
    - low pulse
        - if off, turn on and send high pulse
        - if on, turn off and send low pulse
- &, maintain dictionary of input modules (default to low)
    - if all input are high pulse, then send low pulse
    - else, send high pulse
- broadcast
    - echo pulse to all children
- press the button 1000 times and track low and high pulses
    - return low * high
- watch out for cycles?
'''

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
        self.parents = defaultdict(lambda: 'low')
    
    @property
    def all_inputs_high(self, parents: List[str]) -> bool:
        return all(self.parents[p] == 'high' for p in parent)
    
    def receive_pulse(self, action: Action) -> List[Action]:
        self.parents[action.sender] = action.pulse
        return [Action(self.name, child, 'low' if self.all_inputs_high else 'high') for child in self.children]

class Broadercaster(Module):
    def receive_pulse(self, action: Action) -> List[Action]:
        return [Action(self.name, child, action.pulse) for child in self.children]

modules: Dict[str, Module] = {}

for line in s.split('\n'):
    parent, _children = line.split(' -> ')
    children = _children.split(', ')
    if parent[0] == '%': modules[parent[1:]] = Flip(parent[1:], children)
    elif parent[0] == '&': modules[parent[1:]] = Conjunction(parent[1:], children)
    else: modules[parent] = Broadercaster(parent, children)

def bfs():
    q: Deque[Action] = deque()
    q.append(Action('button', 'broadcaster', 'low'))
    
    while q:
        cur = q.popleft()
        logging.debug(cur)
        
        recv_module = modules[cur.receiver]
        q.extend(recv_module.receive_pulse(cur))
        
bfs()