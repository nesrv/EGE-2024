from functools import cache

a = 2 ** 63 - 1
a = tuple(map(int, str(a)))
len_a = len(a)
print(a)


@cache
def f(s, l, fl):
    if l == 0:
        return s == 159     
    R = 10 if not fl else a[-l] + 1
    S = 0
    for x in range(R):
        S += f(s + x, l - 1, fl and (x == a[-l]))

    return S


print(f(0, len_a, 1))


