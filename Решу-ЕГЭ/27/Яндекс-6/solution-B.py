from math import ceil


f = open("27/Яндекс-6/txt.txt")
# f = open("27/Яндекс-6/27_A.txt")


N, K = map(int, f.readline().split())

PERIMETR = [0]*K

for data in f:
    km, capacity = map(int, data.split())
    PERIMETR[km] += ceil(capacity / 2)

min_len = 0
for i in range(K):
    min_len += min(i, K-i)*PERIMETR[i]

current_len = min_len
all_len = sum(PERIMETR)
half_len = sum(PERIMETR[1:ceil(K/2)])

print(all_len, half_len, min_len)

for i in range(1, K):
    current_len = current_len - (all_len - half_len) - PERIMETR[(i+ceil(K/2)) % K]
    print(2, current_len)
    min_len = min(min_len, current_len)
    half_len = half_len - PERIMETR[i] + PERIMETR[(i+ceil(K/2)) % K]

print(min_len)
