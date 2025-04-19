f = open('27/29 (мусор на кольцевой)/107_27_A.txt')

N = int(f.readline())
S = tuple(int(x) * 3 for x in f)
half_len = len(S) / 2
count = 0
min_dist = 10**10
for i in range(N):
    all_distans = 0
    for i in range(1, int(half_len) + 1):
        if i == half_len:
            all_distans += (S[i] * i)
        else:
            all_distans += (S[i] * i + S[-i] * i)
    min_dist = min(min_dist, all_distans)
    S = S[1:] + (S[0],)  

print(min_dist)
