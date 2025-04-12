def bin_ip(ip):
    return (bin(int(ip))[2:].zfill(8) for ip in ip.split('.'))


ip ='218.194.82.148'
mask = '255.255.255.192'

ip = bin_ip(ip)
mask = bin_ip(mask)

print(*ip)
print(*mask)

# 218 194 82 190

res = '000000'
res = '10111110'

print(int(res, 2))