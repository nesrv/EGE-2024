## Тип 17 [№ 33772](https://inf-ege.sdamgia.ru/problem?id=33772)

Набор данных состоит из нечётного количества пар натуральных чисел.

Необходимо выбрать из каждой пары ровно одно число так, чтобы чётность суммы выбранных чисел совпадала с чётностью большинства выбранных чисел и при этом сумма выбранных чисел была как можно меньше.

Определите минимальную сумму, которую можно получить при таком выборе. Гарантируется, что удовлетворяющий условиям выбор возможен.

Входные данные.

[Файл A](27-A.txt)

[Файл B](27-B.txt)



Первая строка входного файла содержит число N  — общее количество пар в наборе. Каждая из следующих N строк содержит два натуральных числа, не превышающих 10 000.

Пример входного файла:

```
5
15 8
5 11
6 3
7 2
9 14
```
Для указанных данных надо выбрать числа
```
8, 5, 3, 2 и 9
```
Большинство из них нечётны, сумма выбранных чисел равна 27 и тоже нечётна. В ответе надо записать число

```
27
```

```python
f = open('EGE-2024/27/17/27-B.txt')

N = int(f.readline())

f = [list(map(int, x.split())) for x in f]


temp = [] # нечетные разницы
temp2 = [] # четные разницы
sum_max = []


for line in f:
    sum_max.append(max(line))
    difference = abs(line[0] - line[1])
    if difference % 2 == 0:
        temp2.append(difference)
    else:
        temp.append(difference)

even_count = len([x for x in sum_max if x % 2 == 0])
uneven_count = N - even_count

print(even_count, uneven_count)

temp2.sort()
temp.sort()

smax = sum(sum_max)
print('Sum Max', smax)
if (even_count > uneven_count and smax % 2 == 0)\
or (even_count < uneven_count and smax % 2 != 0):
    print('a')
    print(smax)
elif smax % 2 != 0:
    if even_count - uneven_count == 1:
        print(max(smax - temp[0], smax - temp2[0] - temp2[1]))
    elif uneven_count - even_count == 1:
        print(max(smax - temp2[0], smax - temp[0] - temp[1]))
    elif uneven_count - even_count > 1 or even_count - uneven_count > 1:
        print(max(smax - temp2[0], smax - temp[0]))
elif sum(sum_max) % 2 == 0 and uneven_count - even_count == 1:
    print(max(smax - temp2[0], smax - temp[0] - temp[1]))

```
```
Когда получившаяся сумма будет чётной, а количество чётных чисел будет меньше количества нечётных чисел и будет отличаться от количества нечётных чисел на единицу, будем находить две минимальных разницы для ситуации, когда будет убираться два чётных числа temp2[0] и tem2[1], и две минимальных разницы для ситуации, когда будет убираться два нечётных числа temp[0] и temp[1].
```