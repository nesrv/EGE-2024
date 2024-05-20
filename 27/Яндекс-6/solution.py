from math import ceil


# f = open("27/Яндекс-6/txt.txt")
f = open("27/Яндекс-6/27_A.txt")


N, K = map(int, f.readline().split())

PERIMETR = [0]*K

for data in f:
    km, capacity = map(int, data.split())
    PERIMETR[km] += ceil(capacity / 2)
   
# print(PERIMETR)

min_len_kabel = 10**10
for i in range(K):
    current_len_kabel = 0
    for j in range(K):
        current_len_kabel += min(abs(i-j), K-abs(i-j))*PERIMETR[j]
    min_len_kabel = min(min_len_kabel, current_len_kabel)
    print(i)
    
print(min_len_kabel) 

# ответ: 149799 (A)