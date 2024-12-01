from collections import Counter

with open('d.in', 'r') as f:
    ls1, ls2 = zip(*[map(int, line.split()) for line in f])
    ct = Counter(ls2)

print(sum(x*ct[x] for x in ls1))
