
## Задача 38 Тип 26 [№ 51995](https://inf-ege.sdamgia.ru/problem?id=51995)

На складе хранятся кубические контейнеры двух цветов различного размера.

Чтобы сократить занимаемое при хранении место, контейнеры вкладывают друг в друга.

Чтобы вложенные контейнеры было лучше видно, их цвета при вложении обязательно должны чередоваться, то есть нельзя вкладывать контейнер в контейнер такого же цвета.

Один контейнер можно вложить в другой, если размер стороны внешнего контейнера превышает размер стороны внутреннего на 5 и более условных единиц.

Группу вложенных друг в друга контейнеров называют блоком. Количество контейнеров в блоке может быть любым.

Каждый блок, независимо от количества и размера входящих в него контейнеров, а также каждый одиночный контейнер, не входящий в блоки, занимает при хранении одну складскую ячейку.

Зная размеры и цвета всех контейнеров, определите максимально возможное количество контейнеров в одном блоке и минимальное количество ячеек для хранения всех контейнеров.

[Файл](https://inf-ege.sdamgia.ru/get_file?id=150732)

Входные данные

Каждая строка входного файла содержит натуральное число и букву A или B.

Число обозначает размер контейнера в условных единицах, буква  — цвет этого контейнера (буквами A и B условно обозначены два цвета).

В ответе запишите два целых числа: сначала максимально возможное количество контейнеров в одном блоке, затем минимальное количество ячеек для хранения всех контейнеров.



### Решение


```python
f = open('txt.txt')

S = [[int(t[0]), t[1]] for val in f if (t := val.split())]
S.sort(reverse=1)

SKL = []
while len(S) > 0:
    M = [S.pop(0)]
    i = 0
    while i < len(S):
        if M[-1][0] - S[i][0] >= 5 and M[-1][1] != S[i][1]:
            M.append(S.pop(i))
            i -= 1
        i += 1
    SKL.append(M)

print(len(SKL), len(SKL[0]))

f = open('26.txt')
box=[]
cklad =[]
for i in f:
    size, color = i.split()
    box.append([int(size),color])


```

