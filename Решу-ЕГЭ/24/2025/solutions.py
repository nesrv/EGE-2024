# 25-30

# f = open('24 (14).txt')
# ans = 0
# s = f.readline().split('A')
# for i in range (len(s)-1):
#     ans = max(len(s[i])+len(s[i+1])+1,ans)
# print(ans)


# 25-31

# f = open('24 (14).txt')
# ans = 0
# s = f.readline().split('D')
# for i in range (len(s)-1):
#     ans = max(len(s[i])+len(s[i+1])+1,ans)
# print(ans)


# 25-32


# f = open('24 (14).txt').read().split('A')
#
# max_s = 0
# for s in f:
#     if s.count('E')>=3:
#         max_s = max(max_s, len(s))
#
#
# print(max_s)


# 25-33

#
# f = open('24 (14).txt').read().split('E')
#
# max_s = 0
# for s in f:
#     if s.count('A') >= 3:
#         max_s = max(max_s, len(s))
#
# print(max_s)

# 25-34


# f = open('107_24.txt').read().replace('AB','*').replace('CB', '*')
#
# asterix = ""
#
# while asterix in f:
#     asterix += '*'
#
#
# print(len(asterix)-1)


# 25-35

# f = open('24 (14).txt').readline().split('E')
#
# c = 0
# for s in f:
#     if len(s) >= 10 and 'F' not in s:
#         c += 1
#
# print(c)

# 25-36


# 25-37

s = open('24 (14).txt').read()

sogl = 'CDF'
glas = 'AO'

i = 0
c = 0
max_c = 0

while i < len(s):
    if s[i] in sogl and s[i + 1] in glas:
        c += 1
        i += 2
        max_c = max(max_c, c)
    else:
        c = 0
        i += 1

print(max_c)


s = (open('24 (14).txt').read()
     .replace('O', 'A')
     .replace('D','C')
     .replace('F', 'C')
     .replace('CA', '*'))



asterix = ""

while asterix in s:
    asterix += '*'

print(len(asterix)-1)