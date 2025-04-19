from re import *

# 77
s = open("24.txt").read()
# print(s)

# s = '12345678910111278156176777879808182848485'
#
x,y = 78,78
sub_s = '78'

while True:
    if sub_s + str(x + 1) in s:
        sub_s += str(x + 1)
        x += 1
    elif str(y - 1) + sub_s in s:
        sub_s = str(y - 1) + sub_s
        y -= 1
    else:
        break

print(len(sub_s))
