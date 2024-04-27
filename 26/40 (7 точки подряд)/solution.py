import re

f = open('26.txt')
N = int(f.readline())

S = {i: set() for i in range(1, 10 ** 5 + 1)}

for line in f:
    x, y = map(int, line.split())
    S[x].add(y)


tmpl = '\\*{3,}'
l_max = 0
for key, line in S.items():
    if len(line) > 5:
        line = sorted(line)
        total = 0
        st = '*'
        for i in range(len(line) - 1):
            if line[i] == line[i + 1] - 1:
                st += '*'
            else:
                st += ' *'
        c = len(re.findall(tmpl, st))
        if c >= l_max:
            print(st, c, key)
            l_max = c
            x = key

print(l_max, x)
