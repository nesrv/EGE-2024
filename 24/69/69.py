f = open("24/69/69.txt").readline()
s = []
mc = 0
for i in range(len(f)):
    if f[i] in 'AB':
        s.append((f[i], i))

end = max_x = 0
start = s[0][1]
A = 1 if s[0][0] == 'A' else 0
B = 1 if s[0][0] == 'B' else 0

for x in range(1, len(s)-1):
    if s[x][0] == 'A':
        A += 1
    else:
        B += 1
    if A > 2 or B > 2:
        max_x = max(max_x, s[x][1] - start - 1)
        start = s[x-3][1]
        A = 1 if A > 2 else A
        B = 1 if B > 2 else B


print(max_x)
