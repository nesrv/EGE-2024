# f = open("24/67/67.txt").readline()
# s = []
# mc = 0
# for i in range(len(f)):
#     if f[i] in 'AB':
#         s.append((f[i], i))
       
# for x in range(len(s) - 2):   
#     if s[x][0] != s[x+1][0]:
#         mc = max(mc, s[x+2][1] - s[x-1][1] - 1) # длина [- А - В -]
# print(mc)


a = [1,2,3]

d = dict(a)
print(d)