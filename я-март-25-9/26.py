f = open("txt.txt")
print('принтеры запросы')

M, P = map(int, f.readline().split())
M = 5
print(M, P)

lst = [list(map(int, x.split())) for x in f][:10]
lst = [[x[0], x[1], sum(x)] for x in lst]

lst.sort(key=lambda x: (x[0], -x[1], x[2]))


working = lst[:M]

waiting = lst[M:]
print('----working-----')
print(*working, sep='\n')

print('----waiting-----')
print(*waiting, sep='\n')

print('----after-----')
i = 0
pause = 0
while waiting:
    waiting_printer = waiting[i]
    for j in range(0, len(working)):
        # print(waiting_printer[0] > working[i][2])
        if waiting_printer[0] >= working[j][2] + 3:
            working[j] = waiting_printer
            waiting.pop(i)
            break
        else:
            pause += 1
            print('pause', waiting_printer)

    else:

        i+=1
        if i > len(waiting):
            i = 0


# #
print('----working-----')
print(*working, sep='\n')
print(pause)