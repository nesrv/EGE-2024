# 4217 298
# 8 февраль 2025
# В палату мер и весов поступил набор из N гирек.
import itertools
from collections import defaultdict

f = open("txt.txt")
# f = open("26.txt")
n = int(f.readline())

w = [int(x) for x in f]
w.sort()
print(w)

weigths = defaultdict(list)
temp = []
for n, x in enumerate(range(sum(w)),1):
    if w:
        current = w.pop(0)
        temp.append(current)
        if not weigths[current]:
            weigths[current].append(current)
        if not weigths[sum(temp)]:
            weigths[sum(temp)].extend(temp.copy())
    #
    if not weigths[n]:
        delta = sum(temp[:-n+x]) - n
        if delta in temp:
            t = temp[:-1]
            t.remove(delta)
            weigths[n].extend(t)
        else:
            if sum(weigths[n-1]) in temp and delta in temp:
                weigths[n].extend((weigths[n-1], delta))

            print('->', n,  delta, sum(weigths[n-1]), temp)


    # weigths[sum(temp)].extend(temp)
    # if not weigths[n]:
    #     s = find_sum_tuple(temp, n)
    #     if not s:
    #         break
    #     weigths[n].extend(s[0])


print(*sorted(weigths.items()),  sep="\n")

