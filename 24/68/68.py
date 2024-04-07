f = open("24/68/68.txt").readline()
s = []
mc = 0
for i in range(len(f)):
    if f[i] in 'XY':
        s.append((f[i], i))

for x in range(len(s) - 2):
    if s[x][0] != s[x+1][0]:
        mc = max(mc, s[x+2][1] - s[x-1][1] - 1)  # длина [- А - В -]
print(mc)
