from collections import defaultdict

f = open("71.txt")
data = f.read()

letter = "UVWXYZ"


d = defaultdict(list)

for i in range(len(data)):
    if data[i] in letter:
        d[data[i]].append(i)


print(*d.items(), sep='\n______________')

