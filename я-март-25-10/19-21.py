# 19 = 91
from math import dist


# Игроки ходят  очереди  перемещают фишку из точки с координатами (x,y)
# в одну из трёх точек: или в точку с координатами (2x, y), или в
# точку с координатами (x,y+3), или в точку с координатами (x, y+4)

def f(x, y, n):
    if dist((x, y), (0, 0)) > 14 or n > 2:
        return n == 2
    h = f(x * 2, y, n + 1), f(x, y + 3, n + 1), f(x, y + 4, n + 1)
    return all(h) if n == 0 else any(h)


for s in range(1, 14):
    if f(3, s, 0):
        print("#19 =", s)
        break

print('-' * 20)

def f(x, y, n):
    if dist((x, y), (0, 0)) > 14 or n > 3:
        return n == 3
    h = f(x * 2, y, n + 1), f(x, y + 3, n + 1), f(x, y + 4, n + 1)
    return all(h) if n % 2 else any(h)


for s in range(1, 14):
    if f(3, s, 0):
        print("20 =", s)


print('-' * 20)


def f(x, y, n):
    if dist((x, y), (0, 0)) > 14 or n > 4:
        return n == 2 or n ==4
    h = f(2 * x, y, n + 1), f(x, y + 3, n + 1), f(x, y + 4, n + 1)
    return all(h) if n % 2 == 0 else any(h)


for s in range(1, 14):
    if f(3, s, 0):
        print("21 =", s)

