
ip_address = list(map(int, '192.168.128.0'.split('.')))

subnet_mask = list(map(int, '255.255.192.0'.split('.')))

res = [ip1 & ip2 for ip1, ip2 in zip(ip_address, subnet_mask)]


print(*ip_address)
print(*subnet_mask)
print(*res)

# H B A F