# 791 75
f = open("26.txt")
print('принтеры запросы')

M, P = map(int, f.readline().split())

print(M, P)

lst = [list(map(int, x.split())) for x in f]
lst = [[x[0], x[1], sum(x) + 3] for x in lst]

lst.sort(key=lambda x: (x[0], -x[1], x[2]))
working = lst[:M]
waiting = lst[M:]

# [457, 13, 473]
# print('----все-----')
# print(lst[-1], sep='\n')
# #
# #
# exit(100)
#

# print('----печатают-----')
# print(*working, sep='\n')
#

#
# print('----ждут-----')
# print(*waiting, sep='\n')

pause_printer = []

i = 0
pause = 0
c = 0
while waiting:
    waiting_printer = waiting[i]
    # print(i)
    for j in range(0, len(working)):
        if waiting_printer[0] >= working[j][2]:
            working[j] = waiting_printer
            waiting.pop(i)
            c += 1
            working.sort(key=lambda x: x[2])
            i = 0
            break
    else:
        i += 1
        # pause += 1
        if i >= len(waiting):
            pause += 1
            pause_printer.append(waiting_printer)
            waiting.pop(i-1)
            i = 0


# #
# print('----последние M-----')
# print(*working, sep='\n')
# print('----ждут-----', c)
# print(*waiting[:5], sep='\n')
print(pause)
print(len(pause_printer))
