


ip = '137.219.220.63'


ip = map(lambda x: f'{int(x):08b}',ip.split('.'))

print(*ip)