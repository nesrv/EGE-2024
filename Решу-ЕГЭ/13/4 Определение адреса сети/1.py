
ip_address = map(int, '145.92.137.88'.split('.'))

subnet_mask = map(int, '255.255.240.0'.split('.'))


ip_address = [f'{ip:b}'.rjust(8, '0') for ip in ip_address]
subnet_mask = [f'{ip:b}'.rjust(8, '0') for ip in subnet_mask]


print('маска =', *subnet_mask)
print('комп = ', *ip_address)


ip_subnet = int('1000', 2)

print(ip_subnet)

res = '145.92.9.0'

# маска = 11111111 11111111 11110000 00000000
# комп =  10010001 01011100 10001001 01011000
# сеть =  10010001 01011100 10000000 00000000
# сеть =     145     92        128       0


#