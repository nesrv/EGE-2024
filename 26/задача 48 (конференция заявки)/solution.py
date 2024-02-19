f = open('txt1.txt')
N = int(f.readline())
lst = [list(map(int, date.split())) for date in f if date.split()]
lst.sort(key=lambda x: x[1])

res = [lst.pop(0)]

i = 0
while i < len(lst):
    t = lst[i]
    if t[0] >= res[-1][1]:
        res.append(t)
    i += 1

# [989, 991], [994, 1028]]
# 992 1345

for i in range(1, len(lst)):
    if lst[i][0] <= res[-1][0] and lst[i][0] >= res[-2][1]:
        res[-1] = lst[i]


print(len(res), res[-1][1], res[-1], res[-2])
