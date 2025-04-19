from math import ceil
f = open('27/32 (медкомпания биоматериал)/27_B.txt')
N = int(f.readline())
'''
6
1 100
2 200
5 4
7 3
8 2
10 190
'''
points = (
    (next(data), ceil(next(data) / 36))
    for line in f
    if (data := map(int, line.split())))

points = set(points)


min_price = 10**10
i=0
for curren_point in points:
    dist = curren_point[0]
    cur_price = 0
 
    for point in points:
       cur_price += abs(point[0] - dist) * point[1]
    min_price = min(min_price, cur_price)
    print(i)
    i+=1

print(min_price)

