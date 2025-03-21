
mask = 255,255,240,0


ip = 172,17,167,18

mask = map(lambda x: f'{x:08b}', mask)
ip = map(lambda x: f'{x:08b}', ip)

print(*mask)
print(*ip)

max_ip = '10101100', '00010001', '10101111', '11111111'

max_ip = map(lambda x: int(x, 2), max_ip)

print(*max_ip)
# 172 17 175 255
# 172 17 175 254