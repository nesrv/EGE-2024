import re

# s = "BBBBABBAAABBBBBABBABBBAABAAEABBFBBBBABBAAABEBAEBABABBAAABABBABABBA"
s = open("я-март-25-10/24.txt").read()


t = r'(?:[AE][BCDF]+){20,}'

res = re.findall(t, s)

print(*res)