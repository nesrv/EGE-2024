# Тип 19 № 61399
# https://inf-ege.sdamgia.ru/problem?id=61399

def f(s, n, m):
    if s >= 34 or n > 2:
        return n == 2
    if n == 0:
        return f(s + 1, n + 1, 1) and f(s + 2, n + 1, 2) and f(s * 2, n + 1, 2)
    else:
        if m == 1:
            return f(s + 2, n + 1, m) or f(s * 2, n + 1, m)
        elif m == 2:
            return f(s + 1, n + 1, m) or f(s * 2, n + 1, m)       
        return f(s + 1, n + 1, m) or f(s + 2, n + 1, m)


for s in range(1, 100):
    if f(s, 0, 0):
        print(s)
        break
