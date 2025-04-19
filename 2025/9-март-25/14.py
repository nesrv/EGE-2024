for x in range(1000000, 1,-1):
    a = 25 ** 340 + 25 ** 79 - 5 ** 60 + x
    s = 0
    while a:
        a, ost = divmod(a, 25)
        if ost % 25 == 0:
            s += 1
    if s == 287:
        print(x)
        break