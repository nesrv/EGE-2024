# 4217 298
# 8 февраль 2025
# В палату мер и весов поступил набор из N гирек.

f = open("/home/user/projects/EGE-2025/я-февраль-25-8/txt.txt")
# f = open("/home/user/projects/EGE-2025/я-февраль-25-8/26.txt")

n = int(f.readline())

all = [int(x) for x in f]
all.sort()

weights = [all.pop(0)]


for current in all:
    if weights[-1] < current:
        print(weights[-1] +1)
        break
    else:
        weights += [current]


