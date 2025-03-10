import re

data = open("24.txt", 'r').read()

t = '(?:ABA|BAB)+'

all = re.findall(t, data)

result = len(max(all, key = len))

print(result // 3)