def f7(x):
    s = ""
    while x:
        s += str(x % 7)
        x //= 7
    return s[::-1]


for N in range(100, 1, -1):
    R = f7(N)
    if N % 7 == 0:
        R += R[-2:]
    else:
        R += f7(N % 7 * 2)

    R = int(R, 7)
    if R < 220:
        print(N)
        break

# 30