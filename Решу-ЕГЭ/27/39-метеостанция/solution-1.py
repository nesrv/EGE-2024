f = open('39-метеостанция/27B.txt')
print(f.readline())

s = [int(i) for i in f]
s1 = sorted(s,reverse=True)

# print(s1[:10])

for x in s1[:10]: 
  print(x, s.count(x))


print(sum(s1[:2]))