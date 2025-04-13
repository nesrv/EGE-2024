def f(s, n):
    if s <= 87 or n > 2:
        return n == 2
    h = f(s - 2, n + 1), f(s // 2, n + 1)
    return any(h) if n == 1 else all(h)


# for s in range(89, 200):
#     if f(s, 0):
#         print(s)

# 176


def f(s, n):
    if s <= 87 or n > 3:
        return n == 3
    h = f(s - 2, n + 1), f(s // 2, n + 1)
    return any(h) if n % 2 == 0 else all(h)


# for s in range(89, 200):
#     if f(s, 0):
#         print(s)


# 178 179


def f(s, n):
    if s <= 87 or n > 4:
        return n == 2 or n == 4
    h = f(s - 2, n + 1), f(s // 2, n + 1)
    return any(h) if n % 2 else all(h)


for s in range(88, 200):
    if not f(s, 2) and f(s,0):
        print(s)
180

# 176
# 177
# 180
# 181
