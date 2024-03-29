from itertools import *
# alphabet = '89'
# c = 0
# x = 2**62
# print(len(str(x)))
# print (159/19)
# for i in product(alphabet, repeat=18):
#     s = sum(int(x) for x in i)
#     if s == 159:
#         c+=1

# print(c)

# # 50388 + 816

# 9223372036854775808
# y = 9777777777777777777
y = 4611686018427387904
a = 1599999999999999999
b = 9999999999999999999
# c = 0
# for i in range(a,b):
#     s = sum(int(x) for x in str(i))
#     if s == 159:
#         c += 1
#         print(i)
# gen = (x for x in for x in range(a, b) if sum(int(y) for y in str(x)) == 159)
gen = (x for x in range(a,b) if sum(int(a) for a in str(x))==159)

print(next(gen)) 
print(next(gen)) 
