f = open('27.txt')
auto, bus = 80, 20
n = int(f.readline())  # 888 машин
all_auto = []
parking = {
    'A': [],
    'B': []
}

for val in f:
    *t, type = val.split()
    t1, t2 = map(int, t)
    all_auto.append([t1, t1 + t2, type])

all_auto.sort()

count_auto = 0
count_bus = 0

while len(parking['A']) + len(parking['B']) < auto + bus:
    tr = all_auto.pop(0)
    if tr[2] == 'A' and len(parking['A']) < auto:
        parking['A'].append(tr)
        count_auto += 1  # запарковали легковую
    elif tr[2] == 'A' and len(parking['B']) < bus:
        parking['B'].append(tr)
        count_auto += 1  # запарковали легковую
    elif tr[2] == 'B' and len(parking['B']) < bus:
        parking['B'].append(tr)
        count_bus += 1

while all_auto:
    tr = all_auto.pop(0)
    if tr[2] == 'A':
        for i, auto in enumerate(parking['A']):
            if tr[0] >= auto[1]:
                parking['A'][i] = tr
                count_auto += 1  # запарковали легковую
                break
        else:
            for i, auto in enumerate(parking['B']):
                if tr[0] >= auto[1]:
                    parking['B'][i] = tr
                    count_auto += 1  # запарковали легковую
                    break
    else:
        for i, auto in enumerate(parking['B']):
            if tr[0] >= auto[1]:
                parking['B'][i] = tr
                count_bus += 1
                break

print(count_auto, n - count_bus - count_auto)