from random import shuffle

max_s = 0

# s = '63' * 20 +  '5' * 25 + '3' * 20
# s = '3' * 40 + '5' * 25 + '6' * 20
s = '53' * 25 + '3' * 15 + '6' * 20
print(s)
r = sum(map(int, s))
print(r)

while '53' in s or '63' in s:
    if '63' in s:
        s = s.replace('63', '72', 1)
    else:
        s = s.replace('53', '91', 1)
print(s)
r = sum(map(int, s))
print(r)
