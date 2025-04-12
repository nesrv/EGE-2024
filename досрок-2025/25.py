c = 0
for x in range(700_000, 10**10):
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            M = d + x // d
            break
    if M % 10 == 4:
        print(x, M)
        c += 1
        if c == 5:
            break
