# 15 4041
# 6 январь 2025
# Входной файл содержит сведения о задачах, 
# решённых участниками во время соревнования по программированию. 
f = open("26/Я-2025-Я-6/txt-2.txt")
n = int(f.readline())

tasks = {}

for line in f:  
    dt,number, task = line.split()        
    if number not in tasks:
        tasks[number] = [[],dt]
        
    tasks[number][0].append(task)
    tasks[number][1] = dt

# отсортировать словарь по длине списка и времени

tasks = dict(sorted(tasks.items(), key=lambda x: (len(x[1][0]), x[1][1])))

print(*tasks.items(), sep="\n")

# # найти максимальную длину списка с словаре
# max_len = max(len(x[0]) for x in tasks.values())
# print(max_len)

# # отфильтровать словарь по максимальной длине списка
# tasks = dict(filter(lambda x: len(x[1][0]) == max_len, tasks.items()))

# # отсортировать по времени
# tasks = dict(sorted(tasks.items(), key=lambda x: x[1][1]))


# print(*tasks.items(), sep="\n")
