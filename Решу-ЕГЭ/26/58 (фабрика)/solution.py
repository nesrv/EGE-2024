f = open("26_59852.txt")
n = int(f.readline())
k = int(f.readline())
all = list(map(int, f.readlines()))
details = all[:n]
containers = all[n:]
count = 0
max_detail = 0
while details:
    detail = details.pop(0)
    j = 0
    while j < len(containers):
        if detail <= containers[j]:
            count += 1
            containers[j] -= detail  # уменьшаем размер контейнера
            if containers[j] == 0:
                containers.pop(j)
                j -= 1
            max_detail = max(max_detail, detail)
            j += 1
            break
        j += 1
print(count, max_detail)
