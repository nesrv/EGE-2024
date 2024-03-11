net = 192, 168, 32, 160
mask = 255,255,255,240 # в такой ситуации - миним кол-во хостов = 32


net = [f'{ip:b}'.ljust(8, '0') for ip in net]
mask = [f'{ip:b}'.ljust(8, '0') for ip in mask]


print(*net)
print(*mask)


res = int('1111', 2)
print(res)
count=0
for ip in range(res+1):
  if f'{ip:b}'.count('1') % 2 ==0:
    count+=1

print(count)
