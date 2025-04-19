
for n in range(110_250_000, 110_300_000 + 1):
    set_d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            set_d |= {i, n // i}
            if len(set_d) > 2:
                break
    set_d = sorted(set_d)
    if sum(set_d[-2:]) % 10000 == 1002:
        print(n)
