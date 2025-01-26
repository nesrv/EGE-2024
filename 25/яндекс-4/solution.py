c = 0
for x in range(700_000, 10 ** 10):
    set_d = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            set_d.add(d)
            set_d.add(x // d)
        if len(set_d) > 2:
            break
    if len(set_d) == 2:
        delta = max(set_d) - min(set_d)
        if delta <= 15:
            print(x, delta)
            c += 1
            if c > 5:
                break
