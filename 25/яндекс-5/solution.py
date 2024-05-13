# https://education.yandex.ru/ege/variants/7abf7990-4043-4fe4-b5ce-bcc69d714df9/task/25

from itertools import product

ans = []

for a1, a2, a3, a4 in product(range(10), repeat=4):
    x = int(f'4{a1}8{a2}15{a3}16{a4}23')
    if x % 123 == 42:
        ans.append(x)

print(len(ans), max(ans))
