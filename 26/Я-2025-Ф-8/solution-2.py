# 4217 298
# 8 февраль 2025
# В палату мер и весов поступил набор из N гирек. 
from itertools import permutations
f = open("26/Я-2025-Ф-8/txt.txt")
f = open("26/Я-2025-Ф-8/26.txt")
n = int(f.readline())

w = [int(x) for x in f]

set_weight = set()
for x in range(1, 4):
    variants = permutations(w, x)
    for v in variants:
        set_weight.add(sum(v))


for i, x in enumerate(sorted(set_weight),1):
    if i != x:
        print(i)
        break
     
            
