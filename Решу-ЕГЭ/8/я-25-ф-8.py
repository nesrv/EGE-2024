from itertools import product

# Определите количество шестизначных семеричных чисел, в записи которых ровно одна цифра 0,
# а количество остальных чётных цифр чётно.

# 19440
digits = '0123456'

def count_even_digits(num):
    return sum(int(d) % 2 == 0 for d in num if d != '0') % 2 == 0

c = 0
for d in product(digits, repeat=6):
    if d[0] != '0':
        if d.count('0') == 1 and count_even_digits(d):
            c+=1


print(c)

