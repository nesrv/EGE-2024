from re import *
from re import findall


# s = '78-8776-78086x8-678067x6060608x768060776'
s = open("24/2025/77/69932.txt").read().replace('*', 'x')


t = '[768]{1}[7680]*[^0x-]'
add_t = '[-x]?[768]{1}[^0x-]*'
t += 3*add_t
res = findall(t, s) 

print(res)
print(111, max(res, key=len))
print(len(max(res, key=len)))


# print(len("78-8776-78086*8-678067*6060608*768060776"))
# print(len("78-8776-78086x8-678067x6060608x768060776"))
    
