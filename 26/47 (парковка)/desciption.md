
## Задача 46 Тип 26 [№ 56534](https://inf-ege.sdamgia.ru/problem?id=58534)

На парковке имеется 70 мест для легковых автомобилей и 30 мест для микроавтобусов.

Приезжающий на парковку автомобиль занимает любое свободное место соответствующего типа.

При этом если свободных мест для легковых автомобилей нет, то легковой автомобиль занимает свободное место, предназначенное для микроавтобуса, но микроавтобус не может занять место, предназначенное для легкового автомобиля.

Если подходящего места нет, автомобиль уезжает.


### Решение

### способ 1

```python
f = open('26.txt')
auto, bus = 70, 30
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
print(all_auto)


count = 0
while len(parking['A']) + len(parking['B']) < auto + bus:
    tr = all_auto.pop(0)
    if tr[2] == 'A' and len(parking['A']) < auto:
        parking['A'].append(tr)
    elif tr[2] == 'A' and len(parking['B']) < bus:
        parking['B'].append(tr)
    elif tr[2] == 'B' and len(parking['B']) < bus:
        parking['B'].append(tr)
        count+=1



while all_auto:
    tr = all_auto.pop(0)
    if tr[2] == 'A':
        for i, auto in enumerate(parking['A']):
            if tr[0] >= auto[1]:
                parking['A'][i] = tr
                break
        else:
            for i, auto in enumerate(parking['B']):
                if tr[0] >= auto[1]:
                    parking['B'][i] = tr
                    break
    else:
        for i, auto in enumerate(parking['B']):
            if tr[0] >= auto[1]:
                parking['B'][i] = tr
                count += 1
                break



print(len(parking['A']))
print('->', count )

```
