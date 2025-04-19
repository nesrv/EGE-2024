from itertools import product

ip = map(lambda x: f"{int(x):010b}", "20.24.110.42".split("."))
net = map(lambda x: f"{int(x):010b}", "20.24.96.0".split("."))


mask ='1111111111 1111111111 1111100000 0000000000'

print('комп ', *ip)

print('маска',mask) # 123

print('сеть ', *net)

