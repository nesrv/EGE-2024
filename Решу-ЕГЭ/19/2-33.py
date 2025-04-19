# Тип 19 № 58527 https://inf-ege.sdamgia.ru/problem?id=58527

def f(x, y, n):
    if x >= 40 or y >= 40 or n > 1:
        return n == 1
    if x > y:
        return (f(x + 1, y, n + 1)
                or f(x + 2, y, n + 1)
                or f(x + 3, y, n + 1)
                or f(x, y * 2, n + 1))
    elif y > x:
        return (f(x, y + 1, n + 1)
                or f(x, y + 2, n + 1)
                or f(x, y + 3, n + 1)
                or f(x * 2, y, n + 1))
    else:
        return (f(x + 1, y, n + 1)
                or f(x + 2, y, n + 1)
                or f(x + 3, y, n + 1)
                or f(x, y + 1, n + 1)
                or f(x, y + 2, n + 1)
                or f(x, y + 3, n + 1))


s = set()
for x in range(1, 40):
    for y in range(1, 40):
        if f(x, y, 0):
            s.add(x + y)

print(min(s))
