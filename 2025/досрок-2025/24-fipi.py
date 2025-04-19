
from re import findall
s = open("досрок-2025/24_21421.txt").read()

t = '[1-9AB]{1}[0-9AB]{19}'

res = findall(t, s)

print(res)