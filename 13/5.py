mask = 255, 255, 254, 0



mask_bin = [f'{ip:b}'.ljust(8,'0') for ip in mask]


print(*mask_bin)


res = int('111111111', 2)
print(res-1)
