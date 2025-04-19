def f5(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n = n // 5
    return s


max_zero = 0

for x in range(1, 2031):
    x0  = x
    y = 5 ** 100 - x
    y = f5(y)
    zero = y.count('0')
    if zero > max_zero:
        max_zero = zero
        r = x0


print(r, max_zero)


