from itertools import product

c = 0
for x in product('0123456', repeat=6):
    if x[0] != '0' \
            and x.count('0') == 1 \
            and (x.count('2') + x.count('4') + x.count('6')) % 2 == 0:
        c += 1

print(c)
