# 20 - 5 (2 кучи)
# https://inf-ege.sdamgia.ru/problem?id=27763

def f(s1, s2, n):
    if s1 + s2 >= 47 or n > 3:
        return n == 3
    if n == 0 or n == 2:
        return f(s1 + 1, s2 + 2, n + 1) or f(s1 + 2, s2 + 1, n + 1) \
        or f(s1 * 2, s2, n + 1) or f(s1, s2 * 2, n + 1)
    else:
        return f(s1 + 1, s2 + 2, n + 1) and f(s1 + 2, s2 + 1, n + 1) \
        and f(s1 * 2, s2, n + 1) and f(s1, s2 * 2, n + 1)


for s1 in range(1, 37):
    if f(s1, 10, 0):
        print(s1)