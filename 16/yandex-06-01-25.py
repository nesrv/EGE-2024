import sys
sys.setrecursionlimit(10000)

from decimal import Decimal

def f(n):
    if n <= 1:
        return Decimal(1/2)
    else:
        return (n + 1) * f(n - 1)
#

print(f(200)/ f(198))


