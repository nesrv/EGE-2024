# 39168781038

from re import *
s = open('25/Я-25-Ф/24 (5).txt').read()

for c in range(1, 10**10):
    t = r"\d{%s}" % c
    search = findall(t, s)
    print(search)
    if not search:
        break



print(39168781038)