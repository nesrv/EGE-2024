# f = open("27/Яндекс-5/txt.txt")
f = open("27/Яндекс-5/27_A.txt")
f = open("27/Яндекс-5/27_B.txt")
N = f.readline()
storage = []
for box in f:
    box = [int(x) for x in box.split()]
    storage.append(sorted(box))

storage = sorted(storage, key=sum, reverse=1)
print(storage)

result = [storage.pop(0)]
while storage:
    box = storage.pop(0)
    if (result[-1][0] > box[0] and result[-1][1] > box[1] and result[-1][2] > box[2]) or \
        (result[-1][0] > box[0] and result[-1][1] > box[2] and result[-1][2] > box[1]) or \
        (result[-1][0] > box[1] and result[-1][1] > box[0] and result[-1][2] > box[2])  or \
        (result[-1][0] > box[1] and result[-1][1] > box[2] and result[-1][2] > box[0]) or \
        (result[-1][0] > box[2] and result[-1][1] > box[1] and result[-1][2] > box[0]) or\
        (result[-1][0] > box[2] and result[-1][1] > box[0] and result[-1][2] > box[1]):
        result.append(box)

print('=' * 50)
# print(len(result))
print(len(result))
    

