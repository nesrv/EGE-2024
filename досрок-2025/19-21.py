# 19 = 20
def f(s, n):
    if s >= 61 or n > 2:
        return n == 2
    h = f(s + 1, n + 1), f(s + 4, n + 1), f(s * 3, n + 1)
    return any(h) if n == 1 else all(h)


# for s in range(1, 61):
#     if f(s, 0):
#         print(s)
#         break


# 20 = 16, 19
def f(s, n):
    if s >= 61 or n > 3:
        return n == 3
    h = f(s + 1, n + 1), f(s + 4, n + 1), f(s * 3, n + 1)
    return any(h) if n % 2 == 0 else all(h)


# for s in range(1, 61):
#     if f(s, 0):
#         print(s)
    

# 21 = 15


def f(s, n):
    if s >= 61 or n > 4:
        return n == 2 or n == 4
    h = f(s + 1, n + 1), f(s + 4, n + 1), f(s * 3, n + 1)
    return any(h) if n % 2 else all(h)


for s in range(1, 61):
    if f(s, 0):
        print(s)
        break
    