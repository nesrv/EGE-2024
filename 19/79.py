# Тип 19 № 61399
# https://inf-ege.sdamgia.ru/problem?id=61399

def f(s, n):
    if s >= 78 or n > 2:
        return n == 2
    if n == 1:
        return f(s + 1, n + 1) or f(s + 4, n + 1) or f(s * 4, n + 1)
       
    else:
        return f(s + 1, n + 1) and f(s + 4, n + 1) and f(s * 4, n + 1)


for s in range(1, 100):
    if f(s, 0):
        print(s)
        break
