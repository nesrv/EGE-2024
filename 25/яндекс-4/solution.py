A = 700_000

for x in range(A, 10**10):
    set_d = set()
    sqrt_x = int(x ** 0.5)
    for d in range(sqrt_x - 15, sqrt_x + 16):
        if x % d == 0:           
            set_d.add(d)
            set_d.add(x // d)
            if len(set_d) > 4:
                break
    print(x, set_d)
    if len(set_d) == 4:
        print(x, set_d)
        set_d = sorted(set_d)
        delta = set_d[-1] - set_d[0]
        if delta <= 15:
            print(x, delta)
             