import re
# s = 'CABCABABABABCBA'

s = open("24/Яндекс-7/24 (3).txt").read()

t = "(ABA|BAB){9}"

res = re.search(t, s)

print(res)

