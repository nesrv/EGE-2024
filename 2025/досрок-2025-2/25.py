c = 0
for x in range(1_125_000, 10**10):
    if c == 5:
        break
    for d in range(17, x // 2 + 1):
        if x % d == 0 and d % 10 == 7:
            print(x, d)
            c += 1
            break


# 1125003 467
# 1125006 97
# 1125009 17
# 1125011 3187
# 1125012 177