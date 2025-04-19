
from collections import defaultdict

f = open("досрок-2025/26.txt")
# f = open("досрок-2025/26_Досрок_Вост_1П.txt")

N, M, K = map(int, f.readline().split()) 

kino = defaultdict(list)

for data in f:
    row, place = map(int, data.split())
    kino[row].append(place)


print(kino)
# print(*kino.items(), sep="\n")

# print(*kino, sep="\n")

# kino = [''.join(sublist) for sublist in zip(*kino)]

# print()
# print(*kino, sep="\n")



# count_free = 0
# max_free = 0
# for free in kino:
#     max_free = max(max_free, free.count('0'*N))

# print(max_free)
    


