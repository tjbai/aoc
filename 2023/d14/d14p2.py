#!/usr/local/bin/python3

from sys import argv
from typing import List

if len(argv) > 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

# got bored with the problem, so decided to practice some better code design

class Grid:
    def __init__(self, g):
        self.g = g
        self.rot = 0
    
    @property
    def load(self) -> int:
        res, M = 0, len(self.g)
        for r in range(len(self.g)):
            for c in range(len(self.g[0])):
                if self.g[r][c] == 'O': res += M - r
        return res
    
    def slide(self) -> None:
        for c in range(len(self.g[0])):
            insert = 0
            for r in range(len(self.g)):
                if self.g[r][c] == 'O':
                    self.g[r][c] = '.'
                    self.g[insert][c] = 'O'
                    insert += 1
                elif self.g[r][c] == '#':
                    insert = r + 1
        
    def _rot(self, g) -> List[List[str]]:
        return [list(reversed(col)) for col in zip(*g)]
        
    def rotate(self) -> None:
        self.rot = (self.rot + 1) % 4
        self.g = self._rot(self.g)
        
    def __repr__(self) -> str:
        g = self.g[:]
        for _ in range((4 - self.rot) % 4): g = self._rot(g)
        res = ''
        for r in g:
            res += ' '.join(r)
            res += '\n'
        return res
    
    def cycle(self) -> None:
        for _ in range(4):
            self.slide()
            self.rotate()

grid = Grid([list(line) for line in s.split('\n')])

history = []
for rem in range(1000000000):
    grid.cycle()
    
    if grid.load in history:
        i = history.index(grid.load)
        cycle_len = len(history) - i
        offset = rem % cycle_len
        print(history[i+offset])
        print(history)
        break
    
    history.append(grid.load)