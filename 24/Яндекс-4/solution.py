from re import *

# s = 'abcbabcdefgabcdefgh'

s = open("24 (4).txt").read()
t = r'(.).*\1'

res = search(t,s)

print(res)

