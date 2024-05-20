f = open("26/36 (контейнеры)/26.txt")
N = f.readline()
storage = [int(x) for x in f]
storage.sort(reverse=1)

all_boxes = []

while storage:    
    i = 0
    box = [storage.pop(0)]
    while i < len(storage):
        if box[-1] - storage[i] >= 5:
            box.append(storage.pop(i))
            i-=1
        i+=1
    all_boxes.append(box)
         
print(len(all_boxes), len(all_boxes[0]))


