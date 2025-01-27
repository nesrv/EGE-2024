import re

s = 'abcbabcdefgabcdefghвыф3212'
# s = 'acmsee'
# s = open("24 (4).txt").read()
# t = r'(.).*\1'
t = r'b(?!(\w).*\1)\w+'

res = re.search(t,s)

print(res)

