from itertools import product

net = map(lambda x: f"{int(x):010b}", "172.30.0.0".split("."))
mask = map(lambda x: f"{int(x):010b}", "255.254.0.0".split("."))

print(*net)
print(*mask)

c = 0
for x in product("01", repeat=17):
    if (8 + x.count("1")) % 12 != 0:
        c += 1
print(c)
