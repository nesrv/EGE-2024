# https://inf-ege.sdamgia.ru/problem?id=61385


x = 1_222_222_222
y = 1_555_555_666

# 1 способ 
print((y - x) // 2 ** 5 - 1)

# 2 способ
x = f'{x:b}'
y = f'{y:b}'
x = x[:-5]
x = int(x, 2)

y = y[:-5]
y = int(y, 2)
cr = 0
print(y - x - 1)

# 3 способ

for n in range(x, y):
    n2 = f"{n:b}"
    # print(n2, end = '-')
    ost = f"{n % 3:b}"
    ost = ost.rjust(2, '0')
    r = n2 + ost
    r2 = int(r, 2)
    ost1 = f'{r2 % 5:b}'
    ost1 = ost1.rjust(3, '0')
    R1 = r + ost1
    # print(R1)
    R = int(R1, 2)
    if 1_222_222_222 <= R <= 1_555_555_666:
        cr += 1
print(cr)
