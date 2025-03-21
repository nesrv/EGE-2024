
#
# A. Прибавить 1
# B. Умножить на 2
# C. Умножить на 3

def f(x, y):
    if x == y:
        return 1
    if x > y or x == 13:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)



print(f(3, 8) * f(8, 18))


