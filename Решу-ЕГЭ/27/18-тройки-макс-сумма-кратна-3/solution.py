# lst = '''
# 4
# 5
# 8
# 14
# 11
# '''.strip().split('\n')[1:]

# f = open('27/18-тройки-чисел-кратные-3/27-A.txt')
f = open('27/18-тройки-чисел-кратные-3/27-B.txt')

lst = f.readlines()[1:]
lst = [int(x) for x in lst]

lst.sort()


b_0 = [i for i in lst if i % 3 == 0][:3]
b_1 = [i for i in lst if i % 3 == 1][:3]
b_2 = [i for i in lst if i % 3 == 2][:3]

print(b_0, b_1, b_2)

res = 10 ** 10

if len(b_0) > 2:
    res = min(res, sum(b_0[:3]))   
if len(b_1) > 2:
    res = min(res, sum(b_1[:3]))
if len(b_2) > 2:
    res = min(res, sum(b_2[:3])) 

if b_0 and b_1 and b_2:
    res = min(res, min(b_0) + min(b_1) + min(b_2))

print(res)
