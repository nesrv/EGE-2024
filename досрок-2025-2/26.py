# f = open("досрок-2025-2/26.txt")
f = open("досрок-2025-2/26_21424.txt")
f.readline()
shop = [int(x) for x in f]
shop.sort(reverse=1)

pack = [shop.pop(0)]

while shop:
    box = shop.pop(0)
    if pack[-1] - box >= 9:
        pack.append(box)


print(len(pack))
print(pack[-1])
