# 19 = 6


def f(s1, s2, n):
    if s1 + s2 >= 150 or n > 2:
        return n == 2
    h = (
        f(s1 + 2, s2, n + 1),
        f(s1 * 3, s2, n + 1),
        f(s1, s2 + 2, n + 1),
        f(s1, s2 * 3, n + 1),
    )
    return any(h)


# for s1 in range(1, 133):
#     if f(s1,16,0):
#         print(s1)
#         break


# 20 = 4,42


def f(s1, s2, n):
    if s1 + s2 >= 150 or n > 3:
        return n == 3
    h = (
        f(s1 + 2, s2, n + 1),
        f(s1 * 3, s2, n + 1),
        f(s1, s2 + 2, n + 1),
        f(s1, s2 * 3, n + 1),
    )
    return any(h) if n % 2 == 0 else all(h)


# for s1 in range(1, 133):
#     if f(s1,16,0):
#         print(s1)


# 21 = 43


def f(s1, s2, n):
    if s1 + s2 >= 150 or n > 4:
        return n == 2 or n == 4
    h = (
        f(s1 + 2, s2, n + 1),
        f(s1 * 3, s2, n + 1),
        f(s1, s2 + 2, n + 1),
        f(s1, s2 * 3, n + 1),
    )
    return any(h) if n % 2 else all(h)


for s1 in range(1, 133):
    if f(s1, 16, 0):
        print(s1)
        break
