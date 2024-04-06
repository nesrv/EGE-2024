f = open("24/70/70.txt").readline()
s = []
mc = 0
for i in range(len(f)):
    if f[i] in 'CD':
        s.append((f[i], i))

max_x = 0
start = s[0][1]
C = 1 if s[0][0] == 'C' else 0
D = 1 if s[0][0] == 'D' else 0

for x in range(1, len(s)-1):
    if s[x][0] == 'C':
        C += 1
    else:
        D += 1
    if C > 2 or D > 2:
        max_x = max(max_x, s[x][1] - start - 1)
        start = s[x-2][1]
        C = 1 if C > 2 else C
        D = 1 if D > 2 else D
       


print(max_x)
