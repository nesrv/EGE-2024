def F(n):
    if n <= 1:
        return 1
    if n % 2 == 0 and n > 1:
        return F(n - 1) / 3
    if n % 2 != 0 and n > 1:
        return 6*F(n - 1)


for i in range(0, 10):
    print(F(i), i)


#Никита Муравский 

from sys import setrecursionlimit
setrecursionlimit(10**5)
from functools import lru_cache
@lru_cache
def F(n):
    if n <= 1: return 1
    else:
        if n % 2 == 0: return F(n - 1) / 3
        else: return F(n - 1) * 6

def F_simplified(n):
    return 2 ** ((n-1) // 2)
def F_simplified_B(n):
    return 2 ** ((n-1) // 2 + 1 ) // 6
for i in range(0, 100):
    print(F(i), i, F_simplified(i))
#print( F(2049) / F(2046) )
print(F_simplified(2049) / F_simplified_B(2046))
