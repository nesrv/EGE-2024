# 7555448
# 7555442 + 6

def f(n):
    if n == 1:
        return 2
    if n > 1 and f(n - 1) < 7555444:
        return f(n - 1) + 6
    return f(n - 1) - 7555444


def f2(n):
    return 2 + 6 * (n - 1)



print(f2(10))
for x in range(1,10**10):
    if f2(x) > 7555444:
        print(x)
        break

print(f2(1259242))

