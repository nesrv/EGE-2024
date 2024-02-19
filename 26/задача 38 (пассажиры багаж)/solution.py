f = open('txt1.txt')

k = int(f.readline())  # 210 ячейки
n = int(f.readline())  # 987 кол-во пассажиров

all_bagage = []

for val in f:
    t1, t2 = map(int, val.split())
    all_bagage.append([t1, t2])

all_bagage.sort(key=lambda x: x[0])

camera = all_bagage[:k]
all_bagage = all_bagage[k:]
print(camera)
print(all_bagage)

count = k
while len(all_bagage) > 0:
    i = 0
    bagage = all_bagage.pop(0)
    while i < k:
        if bagage[0] > camera[i][1] and bagage[1] < 1440:
            camera[i] = bagage
            count += 1
            num = i
            break
        i += 1

print(count, num + 1)
print(len(camera))