from collections import Counter

with open('d.in', 'r') as f: lines = f.readlines()
ls1, ls2 = zip(*[map(int, line.split()) for line in lines])
ct = Counter(ls2)

print(sum(x*ct[x] for x in ls1))
