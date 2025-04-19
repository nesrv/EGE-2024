f = open('27/29 (мусор на кольцевой)/txt.txt')
# f = open('27/29 (мусор на кольцевой)/107_27_B.txt')

N = int(f.readline())

points = [int(x) * 3 for x in f]
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



distanse[0] = sum_0

for i in range(1, N):
    shift = left_sum - right_sum
    left_point = points[(i + (N // 2) - 1) % N]
    right_point = points[(i - (N // 2)) % N]
   
    distanse[i] = distanse[i - 1] + points[i - 1] - left_point + shift
    right_sum += left_point - points[i] 
    left_sum += points[i-1] - right_point

print(min(distanse))
