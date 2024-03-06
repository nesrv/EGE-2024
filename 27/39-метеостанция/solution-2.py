f = open('39-метеостанция/27B.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]
m = 0
maxi = 0

for i in range(N - K):  
    m = max(m, a[i + K])
    maxi = max(maxi, a[i] + m)  
print(maxi)
