# №29 Тип 20 № 52191 https://inf-ege.sdamgia.ru/problem?id=52191


def f(x, y, n):
    if x + y > 60 or n > 3:
        return n == 3
    if n % 2 == 0:
        if x > y:
            return f(x, y + 1, n + 1) or f(x, y + 2, n + 1) or f(x, y * 2, n + 1)
        else:
            return f(x + 1, y, n + 1) or f(x + 2, y, n + 1) or f(x * 2, y, n + 1)
    else:
        if x > y:
            return f(x, y + 1, n + 1) and f(x, y + 2, n + 1) and f(x, y * 2, n + 1)
        else:
            return f(x + 1, y, n + 1) and f(x + 2, y, n + 1) and f(x * 2, y, n + 1)


for x in range(1, 53):
    if f(8, x, 0):
        print(x)