from sys import setrecursionlimit

setrecursionlimit(10000)

def F(n):
    if n > 2025:
        return 1
    else:
        return 2 * n + F(n + 2)

result = F(23) - F(20)
print(result)
    