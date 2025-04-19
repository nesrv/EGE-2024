mask = 255, 255, 255, 224
addr = 162, 196, 0, 157


mask_bin = [f'{ip:b}'.ljust(8, '0') for ip in addr]
addr_bin = [f'{ip:b}' for ip in mask]


print(*addr_bin)
print(*mask_bin)

all_addr = 2 ** 5

res = int('11101', 2)
print(res)
