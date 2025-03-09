# 791 75
f = open("26.txt")
print('принтеры запросы')

M, P = map(int, f.readline().split())

print(M, P)

lst = [list(map(int, x.split())) for x in f]
lst = [[x[0], x[1], sum(x) + 3] for x in lst]

lst.sort(key=lambda x: (x[0], -x[1]))
lst_working = lst[:M]

lst_working.sort(key=lambda x: x[2])

lst_waiting = lst[M:]

[457, 13, 473]
print('----печатают-----')
print(*lst_working, sep='\n')

print('----ждут-----')

print(*lst_waiting[:M], sep='\n')
print('----последние M-----')
print(lst_waiting[-3:], sep='\n')
pause = 0

while lst_waiting:
    waiting_p = lst_waiting.pop(0)
    working_p = lst_working.pop(0)
    if working_p[2] < waiting_p[0]:
        pause +=1
    lst_working.append(waiting_p)
    lst_working.sort(key=lambda x: x[2])






# #
# print('----последние M-----')
# print(*working, sep='\n')
# print('----ждут-----', c)
# print(*waiting[:5], sep='\n')
print(pause, working_p)

