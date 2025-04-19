f = open("досрок-2025/17.txt")

lst = [int(x) for x in f]

max_21 = max(x for x in lst if abs(x) % 100 == 21) ** 2


def f(x):
    return abs(x) % 100 == 21 and 10_000 <= abs(x) < 100_000


c = 0
max_s = 0
for i in range(len(lst) - 1):
    a, b = lst[i], lst[i + 1]
    if f(a) ^ f(b) and (a**2 + b**2) >= max_21:
        c += 1
        max_s = max(max_s, a + b)


print(c, max_s)


# 74 103365
