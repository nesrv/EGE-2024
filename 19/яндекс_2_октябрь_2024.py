def f(s1, s2, n):
    if s1 + s2 >= 231 or n > 2:
        return n == 2
    h = (
        f(s1 + 4, s2, n + 1),
        f(s1, s2 + 4, n + 1),
        f(s1 * 3, s2, n + 1),
        f(s1, s2 * 3, n + 1),
    )
    return any(h)


for s in range(1, 218):
    if f(10, s, 0):
        print(s)  # 25
        break

# -----------------------


def f(s1, s2, n):
    if s1 + s2 >= 231 or n > 3:
        return n == 3
    h = (
        f(s1 + 4, s2, n + 1),
        f(s1, s2 + 4, n + 1),
        f(s1 * 3, s2, n + 1),
        f(s1, s2 * 3, n + 1),
    )
    return any(h) if n % 2 == 0 else all(h)


for s in range(1, 218):
    if f(10, s, 0):
        print(s)  # 66 69


print("======21====== ")



def f(s1, s2, n):
    if s1 + s2 >= 231 or n > 4:
        return n == 2 or n==4
    h = (
        f(s1 + 4, s2, n + 1),
        f(s1, s2 + 4, n + 1),
        f(s1 * 3, s2, n + 1),
        f(s1, s2 * 3, n + 1),
    )
    return any(h) if n % 2 else all(h)


for s in range(1, 218):
    if f(10, s, 0):
        print(s)  #  62 70 ? 73
