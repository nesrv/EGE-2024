import sys 


sys.setrecursionlimit(10000) 

from decimal import Decimal

def f(n):
    if n <= 1:
        return Decimal(0.5)
    else:
        return (n + 1) * f(n - 1)

s = []

r = f(200)/f(198)

print(r)
    


