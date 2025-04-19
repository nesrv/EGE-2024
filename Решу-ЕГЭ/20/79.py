# Тип 19 № 61399
# https://inf-ege.sdamgia.ru/problem?id=61399

def f(s, n, m):
    if s >= 34 or n > 3:
        return n == 3
    if n == 0:
        return f(s + 1, n + 1, 1) or f(s + 2, n + 1, 2) or f(s * 2, n + 1, 3)
    if n == 1:
        if m == 1:
            return f(s + 2, n + 1, 2) and f(s * 2, n + 1, 3)
        elif m == 2:
            return f(s + 1, n + 1, 1) and f(s * 2, n + 1, 3)
        return f(s + 1, n + 1, 1) and f(s + 2, n + 1, 2)
    if n == 2:
        if m == 1:
            return f(s + 2, n + 1, 2) or f(s * 2, n + 1, 3)
        elif m == 2:
            return f(s + 1, n + 1, 1) or f(s * 2, n + 1, 3)
        return f(s + 1, n + 1, 1) or f(s + 2, n + 1, 2)


for s in range(1, 100):
    if f(s, 0, 0):
        print(s)
