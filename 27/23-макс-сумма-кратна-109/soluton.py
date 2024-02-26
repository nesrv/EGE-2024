f = open('27/23-макс-сумма-кратна-109/txt.txt')
# f = open('27/23-макс-сумма-кратна-109/27_B.txt')
N = int(f.readline())
lst = [int(x) for x in f]

'''
8 2 3 4 93 42 34 5 95
'''
s = 0

min_s = {0: (0, 0)}
res = []
d = 89
for i, x in enumerate(lst, 1):
    s += x
    if s % d not in min_s:
        min_s[s % d] = (s, i)
    else:
        res.append([s-min_s[s % d][0], min_s[s % d][1] - i])


print(-max(res)[1])
print(res)
print(min_s)
