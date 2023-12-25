#!/usr/local/bin/python3

# NOTE: lots of OOP for practice

import os
import logging
from math import lcm
from dataclasses import dataclass
from itertools import pairwise
from abc import ABC, abstractmethod
from collections import defaultdict, deque, Counter
from typing import List, Literal, Dict, Deque, Tuple

logging.basicConfig(
    level='DEBUG' if os.environ.get('LOG') == '1' else 'INFO',
    format='%(lineno)s:%(funcName)s:%(message)s'
    )

logger = logging.getLogger(__name__)

##################################################

input_file = 'd.in'
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
    
    def __repr__(self) -> str:
        return f'FLIP: {super().__repr__()}'
    
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
    
    def __repr__(self) -> str:
        return f'CONJ: {super().__repr__()}'

class Broadercaster(Module):
    def receive_pulse(self, action: Action) -> List[Action]:
        return [Action(self.name, child, action.pulse) for child in self.children]

modules: Dict[str, Module] = {}
parents: Dict[str, List[str]] = defaultdict(list)

def show_parents(s: str) -> List[Module]:
    return [modules[p] for p in parents[s]]

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

# return everything that turned on
def bfs() -> List[str]: 
    ons = []
    q: Deque[Action] = deque()
    q.append(Action('button', 'broadcaster', 'low'))
    
    while q:
        cur = q.popleft()
        logging.debug(cur)
        if cur.receiver == 'dg' and cur.pulse == 'high': ons.append(cur.sender)
        if cur.receiver not in modules: continue
        recv_module = modules[cur.receiver]
        q.extend(recv_module.receive_pulse(cur))
        
    return list(ons)


# just brute force the parents
ps = set(parents['dg'])

# run for a bunch of iters
ons: Tuple[int, str] = []
for i in range(20_000):
    ons.extend((i, p) for p in bfs())
    
for p in ps: print(Counter(b-a for a, b in pairwise(x for x, y in ons if y == p)))

# visual inspection yields 4051, 3929, 3767, 3823
print(lcm(4051, 3929, 3767, 3823))