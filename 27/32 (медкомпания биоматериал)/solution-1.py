from math import ceil
f = open('27/32 (медкомпания биоматериал)/txt.txt')
N = int(f.readline())

points = [
    [next(data), ceil(next(data) / 96)]
    for line in f
    if (data := map(int, line.split()))]

print(*points)

min_price = 10**10
for curren_point in points:
    dist = curren_point[0]
    cur_price = 0
    for point in points:
        if curren_point != point:
            cur_price += abs(point[0] - dist) * point[1]
    min_price = min(min_price, cur_price)

print(min_price)
print(8+6+5+3+10)
