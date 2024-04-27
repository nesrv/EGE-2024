
## Задача 58 Тип 26 [№ 59852](https://inf-ege.sdamgia.ru/problem?id=60967)

Главному инженеру фабрики дали задачу написать программу для раскладки N деталей в K контейнеров, каждый из которых рассчитан на свой определённый объём.

Все детали кладут по очереди. Каждую следующую деталь стараются положить в контейнер с наименьшим возможным номером.

Укажите в ответе два числа: количество отложенных деталей и максимальный объём детали, которую смогли положить.


### Решение

#### способ 1

```python
f = open("26_59852.txt")
n = int(f.readline())
k = int(f.readline())
all = list(map(int, f.readlines()))
details = all[:n]
containers = all[n:]
count = 0
max_detail = 0
for i in range(n):
    for j in range(k):
        if details[i] <= containers[j]:
            count += 1
            containers[j] -= details[i] # уменьшаем размер контейнера
            max_detail = max(max_detail, details[i])
            break
print(count, max_detail)

```

#### способ 2

```python
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



```
