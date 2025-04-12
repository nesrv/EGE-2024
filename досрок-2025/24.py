
from re import findall
f = open("досрок-2025/24_2.txt").read()

t = '[1-9AB]{16}'

all = findall(t, f)

# print(all)

res = {}
for x in all:
    y = int(x, 12)
    if y % 6 == 0:
        res[y] = x    



print(res)


print(len('8445916B299163616'))
# 8445916B299163616