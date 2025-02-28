# 963

def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    if x % 3:
        return f(x - (x % 3), y) + f(x - 5, y)
    if x % 3 == 0:
        return f(x // 3, y) + f(x - 5, y)


print(f(103, 73) * f(73, 24))

