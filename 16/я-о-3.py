import sys


sys.setrecursionlimit(10000)

from decimal import Decimal


c = 0


def f(n):
    if n == 41:
        return 41
    if n > 41 and n % 2 == 0:
        return f(n - 1) - n
    else:
        return n * f(n - 2)


r = f(9094) // f(9089)


print(r)