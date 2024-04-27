f = open("26/задача 42 (камера хранения)/26.txt")

K = int(f.readline())
N = int(f.readline())
sklad = []


for i in f:
    x,y = map(int, i.split())
    sklad.append((x,y))
sklad.sort()


kamera = sklad[:K]
sklad = sklad[K:]

counter = K

while sklad:
    box = sklad.pop(0)
    i = 0
    while i < len(kamera):
        if box[0] > kamera[i][1]:
            kamera[i] = box
            counter += 1
            last = i
            break
        i += 1

print(counter)
print(last + 1) # ячейки пронумерованы с 1
