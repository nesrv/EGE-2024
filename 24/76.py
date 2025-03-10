import re

f = open("24.69902.txt")
s = f.read()

s = s.replace('DE', 'D E').split()

maxi = 0
for i in range(len(s)):
    r = ''.join(s[i:i + 241])
    maxi = max(maxi, len(r))
print(maxi)

