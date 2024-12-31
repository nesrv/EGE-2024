for x in range(112_500_00, 112_550_000 + 1):
    set_d = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            set_d. add(x // d)
            if len(set_d) == 2:
                break
    if set_d and sum(set_d) % 10_000 == 1214:
        print(x)
