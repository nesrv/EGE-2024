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
