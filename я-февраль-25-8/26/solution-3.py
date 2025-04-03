# 4217 298
# 8 февраль 2025
# В палату мер и весов поступил набор из N гирек.
import itertools
from collections import defaultdict
from math import prod

f = open("txt.txt")
# f = open("26.txt")
n = int(f.readline())

all = [int(x) for x in f]
# w.sort()

weigths = defaultdict(int)

for w in all:
    weigths[w] += 1

weigths = dict(sorted(weigths.items()))
print(*weigths.items(),  sep="\n")
print()
