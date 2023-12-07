#!/usr/bin/python3

from sys import argv
from collections import defaultdict

if len(argv) == 1: input_file = 'd.in'
else: input_file = 'sample.in'

with open(input_file) as f: s = f.read() 

cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
card_ranks = {c: i for i, c in enumerate(cards)}

def hand_strength(s: str) -> int:
    if s == 'JJJJJ': return 6
    most_freq = 0
    freq = defaultdict(int)
    js = 0
    
    for c in s:
        if c == 'J':
            js += 1
            continue
        freq[c] += 1
        most_freq = max(most_freq, freq[c])
        
    most_freq += js
    if len(freq) == 1: return 6
    elif len(freq) == 2: return 5 if most_freq == 4 else 4
    elif len(freq) == 3: return 3 if most_freq == 3 else 2
    elif len(freq) == 4: return 1
    return 0

def ranks(s: str) -> list:
    return [card_ranks[c] for c in s]

ls = []
for line in s.split('\n'):
    hand, _bid = line.split()
    bid = int(_bid)
    ls.append((hand_strength(hand), *ranks(hand), hand, bid))
ls.sort()

res = 0
for i, (strength, *_, hand, bid) in enumerate(ls): res += bid * (i + 1)
print(res)