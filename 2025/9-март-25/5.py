
from math import prod
for N in range(1000, 10000):
    R = str(N)
    R = R.replace('3', '4')
    R = R.replace('7', '8')
    R = prod(map(int, R))
    if R == 256:
        print(N)
        break


# 1377

