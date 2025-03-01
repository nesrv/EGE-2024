from random import shuffle


max_s = 0
for _ in range(10**6):
    s = '3' * 40 + '5' * 25 + '6' * 20
    s = list(s)
    shuffle(s)
    s = ''.join(s)

    while '53' in s or '63' in s:
        if '63' in s:
            s = s.replace('63', '72', 1)
        else:
            s = s.replace('53', '91', 1)


    s = sum(map(int, s))
    max_s = max(max_s, s)

print(max_s)