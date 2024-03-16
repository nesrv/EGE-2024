from itertools import *


c1 = '1357'
c2 = '2468'
count = 0
for i in product(c1, c2, c1, c2, c1, c2, c1, c2, c1):
    s = ''.join(i)
    for j in c1 + c2:
        if s.count(j) > 3:
            break
    else:
        count += 1

print(count * 2)
