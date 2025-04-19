# 77
s = open("24.txt").read()

t = ''
for x in range(78, 200):
    t += str(x)
    if t in s:
        temp = t

t = temp
for x in range(77, 0, -1):
    t = str(x) + t
    if t in s:
        temp = t


print(len(temp))


