from itertools import *

net = '212.192.32.96'.split('.')
mask = '255.255.255.224'.split('.')


def f(x):
    return f'{int(x):b}'.zfill(8)


net = map(f, net)
mask = map(f, mask)

print(*net)
print(*mask)

all_ip = product('01', repeat=5)
c = 0
for ip in all_ip:
    ip =  ''.join(ip)
    if (not '000' in ip) and (not '111' in ip):
        print(ip)
        c += 1


print(c)
