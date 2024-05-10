'''
может возникнуть ситуация, когда получившаяся сумма будет чётной, 
а количество чётных чисел будет меньше количества нечётных чисел и 
будет отличаться от количества нечётных чисел на единицу, 
Тогда будем находить две минимальных разницы для ситуации,
когда будет убираться два чётных числа, 
и две минимальных разницы для ситуации, когда будет убираться два нечётных числа   
'''

f = open("27/16 (четность суммы пар)/27-A.txt")
n = int(f.readline())

odd = 0  # нечетные

min_odd = []
min_even = []
all_numbers = []

for i in f:
    x, y = map(int, i.split())
    z = max(x, y)
    all_numbers.append(z)
    odd += z % 2

    abs_xy = abs(x - y)
    if abs_xy != 0:
        if abs_xy % 2 == 0:
            min_even.append(abs_xy)
        else:
            min_odd.append(abs_xy)


even = n - odd
min_odd.sort()
min_even.sort()

sum_all_numbers = sum(all_numbers)


if (sum_all_numbers % 2 == 0 and even > odd) or (sum_all_numbers % 2 != 0 and odd > even):
    print(sum_all_numbers)

if even - odd == 1 and sum_all_numbers % 2 != 0:
    print(max(sum_all_numbers-min_odd[0], sum_all_numbers - min_even[0]-min_even[1]))

if odd - even == 1 and sum_all_numbers % 2 == 0:
    print(max(sum_all_numbers-min_even[0], sum_all_numbers - min_odd[0]-min_odd[1]))

else:
    print(sum(all_numbers) - min_odd[0])
