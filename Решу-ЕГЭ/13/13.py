ip_addr = 98,162,71,94
net_addr = 98,162,71,64 # в такой ситуации - миним кол-во хостов = 32


ip_addr = [f'{ip:b}'.ljust(8, '0') for ip in ip_addr]
net_addr = [f'{ip:b}'.ljust(8, '0') for ip in net_addr]


print(*ip_addr)
print(*net_addr)



res = int(ip_addr[-1],2) & int(net_addr[-1],2)
# res = int('1111111', 2)
print(res)
