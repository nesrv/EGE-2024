# Система задних звёзд велосипеда называется кассетой ...

# f = open("26/Яндекс-6/txt.txt")
f = open("26/Яндекс-6(звезды велосипеда)/26.txt")
N = f.readline()
storage = [int(x) for x in f]
storage.sort()
all_stars = []

while storage:
    star = [storage.pop(0)]
    i = 0
    while i < len(storage):
        percent = star[-1] * 0.1
        # print(percent)
        if storage[i] >= star[-1] + percent:
            star.append(storage.pop(i))
            i-=1
        i+=1
    all_stars.append(star)
  

print(len(all_stars[0]), all_stars[0][-1])


