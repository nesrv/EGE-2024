from sys import setrecursionlimit

setrecursionlimit(10000)


def f(n):
    if n > 3000:
        return n
    return f(n + 2) +2

r = f(40) - f(44)

print(r) #4
