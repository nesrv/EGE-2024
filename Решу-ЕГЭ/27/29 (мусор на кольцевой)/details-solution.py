f = open('27/29 (мусор на кольцевой)/txt.txt')

N = int(f.readline())

points = [int(x) for x in f]
print(points)

distanse = [0] * N
right_sum = 0
left_sum = 0
sum_0 = 0


for i in range(1, N // 2 + 1):
    if i == N / 2:
        sum_0 += (points[i] * i)
    else:
        sum_0 += (points[i] * i + points[-i] * i)
    
    right_sum += points[i]
    left_sum += points[N - i]


print(sum_0, right_sum, left_sum)

distanse[0] = sum_0

for i in range(1, N):
    shift = left_sum - right_sum
    left_point = points[(i + (N // 2) - 1) % N]
    right_point = points[(i - (N // 2)) % N]
    print('pp->', left_point, right_point)
    distanse[i] = distanse[i - 1] + points[i - 1] - left_point + shift
    right_sum += left_point - points[i] 
    left_sum += points[i-1] - right_point
    print(distanse[i], right_sum, left_sum)

print(min(distanse))
