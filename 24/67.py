f = open("C:/Users/HUAWEI/Downloads/24 (12).txt").readline()
# s = f.replace('A','*').replace('B','*').split('*')
# print(len(max(s, key= len)) )
s = []
mc = 0
for i in range(len(f)):
    if f[i] in 'AB':
        s.append((f[i], i))
for x in range(len(s) - 1):
   
    if s[x][0] != s[x+1][0]:
        mc = max(mc,s[x+1][1] - s[x][1])
print(mc)