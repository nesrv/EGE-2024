lst = '''
0
4
5
8
14
11
'''.strip().split('\n')
lst = [int(x) for x in lst]
lst.sort()
print(lst)
b_0 = [i for i in lst if i % 3 == 0][-3:]
b_1 = [i for i in lst if i % 3 == 1][-3:]
b_2 = [i for i in lst if i % 3 == 2][-3:]

print(b_0, b_1, b_2)

print(max(sum(b_0), sum(b_1), sum(b_2), b_1[-1] + b_2[-1] + b_0[-1]))
