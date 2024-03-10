# Тип 19 № 61399
# https://inf-ege.sdamgia.ru/problem?id=61399

def f(s, n):
    if s >= 84 or n > 2:
        return n == 2
    if n == 1:
        return f(s + 1, n + 1) or f(s * 2, n + 1) if s % 2 \
        else f(s + 1, n + 1) or f(s * 1.5, n + 1) 
       
    else:
        return f(s + 1, n + 1) and f(s * 2, n + 1) if s % 2 else \
          f(s + 1, n + 1) and f(s * 1.5, n + 1)


for s in range(84, 1,-1):
    if f(s, 0):
        print(s)
        break
