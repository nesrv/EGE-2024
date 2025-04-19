# 791 75
f = open("26.txt")
print('принтеры запросы')

M, P = map(int, f.readline().split())

print(M, P)

lst = [list(map(int, x.split())) for x in f]
lst = [[x[0], x[1], sum(x) + 3] for x in lst]

lst.sort(key=lambda x: (x[0], -x[2]))
working = lst[:M]


working.sort(key=lambda x: (x[2], -x[1]))
waiting = lst[M:]

print('----печатают-----')
print(*working, sep='\n')
#
# #
#
# print(*waiting, sep='\n')

# exit(100)
#
# print('----ждут-----')
# print(*waiting, sep='\n')


i = 0
pause = 0
c = 0
while waiting:
    waiting_printer = waiting.pop(0)
    working_printer = working.pop(0)
    if working_printer[2] <= waiting_printer[0]:
        pause += 1
        print('занят', working_printer,  'ждет', waiting_printer)
    working.append(waiting_printer)
    working.sort(key=lambda x: (x[2]))




# #
# print('----последние M-----')
# print(*working, sep='\n')
# print('----ждут-----', c)
# print(*waiting[:5], sep='\n')
print(pause)

