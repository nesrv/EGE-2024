# 19 = 91
def f(s, n):
    if s > 105 and n == 3:
        return 1
    if s in range(97, 106) or n > 2:
        return n == 2
    h = f(s + 3, n + 1), f(s + 5, n + 1), f(s * 3, n + 1)
    return all(h) if n == 0 else any(h)


for s in range(96, 1, -1):
    if f(s, 0):
        print("#19 =", s)
        break

print('-' * 20)


# 20 = 30 и 88

def f(s, n):
    if s > 105 and n in (2, 4):
        return 1
    if s > 105 and n in (1,3):
        return 0
    if s in range(97, 106) or n > 3:
        return n == 3
    h = f(s + 3, n + 1), f(s + 5, n + 1), f(s * 3, n + 1)
    return all(h) if n % 2 else any(h)

#
for s in range(1, 97):
    if f(s, 0):
        print("#20 =", s)


# 21 = 3
print('-' * 20)
def f(s, n):
    if s > 105 and n in (1,3,5):
        return 1
    if s > 105 and n in (2,4):
        return 0

    if s in range(97, 106) or n > 4:
        return n == 4 or n == 2
    h = f(s + 3, n + 1), f(s + 5, n + 1), f(s * 3, n + 1)
    return all(h) if n % 2 == 0 else any(h)

#
for s in range(1, 97):
    if f(s, 0):
        print("#21 =", s)
