from itertools import product
def f(ip):  
    return (f'{int(ip):b}'.zfill(8) for ip in ip.split('.'))




net = '95.112.224.0'
mask = '255.255.255.128'


net = f(net)
mask = f(mask)
print(*net)
print(*mask)

# 00000000
# 01000010
# 01100110
# 01011010
# 01111110
# 00111100
# 00011000
# 00011000


