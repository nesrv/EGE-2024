from itertools import *

w = "КАБИНЕТ"


words = permutations(w)

c = 0
for word in words:
    if word[-1] not in "АИЕ":
        c += 1

print(c)
