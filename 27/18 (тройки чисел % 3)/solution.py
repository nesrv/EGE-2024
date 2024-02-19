f = open('EGE-2024/27/14/27-B.txt')
N = f.readline()

sum_1 = sum_2 = sum_3 = 0
mindiverens = []
for data in f:
    data = sorted(map(int, data.split()))
    diverens = min(data[2] - data[1], data[2] - data[1])
    if diverens != 0 and diverens not in mindiverens:
        mindiverens.append(diverens)
    sum_1 += data[0]
    sum_2 += data[1]
    sum_3 += data[2]

mindiverens.sort()


if sum_1 % 2 == sum_2 % 2:
    sum_3 -= mindiverens[0]

print(sum_3)