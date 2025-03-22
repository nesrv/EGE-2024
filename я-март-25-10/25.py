simple_div = []

for i in range(2, 20_000):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:

        simple_div.append(i)

c = 0
for x in range(500_000, 10 ** 10):
    R = 0

    for d in simple_div:
        if x % d == 0:
            R += d
            if R > 2_000 and R % 10 == 7:
                print(x, R)
                c += 1
                break
    if c == 5:
        break

'''
500005 9107
500019 12837
500031 7947
500110 3867
500127 3597
'''
