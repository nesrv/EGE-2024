from math import ceil
# f = open('27/32 (медкомпания биоматериал)/txt.txt')
f = open('27/32 (медкомпания биоматериал)/27_B.txt')
N = int(f.readline())

points = [
    [next(data), ceil(next(data) / 36)]
    for line in f
    if (data := map(int, line.split()))]

r_sum = 0
l_sum = 0

prices = [0] * N
for i in range(1, N):
    prices[0] += (points[i][0] - points[0][0]) * points[i][1]
    r_sum += points[i][1]

# print(r_sum)

for i in range(1, N):
    l_sum += points[i - 1][1]
    prices[i] = prices[i - 1] - r_sum * (points[i][0] - points[i - 1][0]) + l_sum * (points[i][0] - points[i - 1][0])
    r_sum -= points[i][1]

print(min(prices))



