f = open("26/35 коробки/txt.txt")
N = f.readline()
storage = [int(x) for x in f]
storage.sort(reverse=1)
boxes = [storage.pop(0)]

while storage:
    box = storage.pop(0)
    if boxes[-1]- box >= 3:
        boxes.append(box)

print(boxes)