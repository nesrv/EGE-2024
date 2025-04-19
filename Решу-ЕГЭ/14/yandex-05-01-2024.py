
max_s = 0
r = {}
for x in '0123456789ABCD':
    for y in '0123456789ABCD':
        z = int('14' + y + '5' + x + '2', 14) + int('31' + x + '2' + y + '3', 14)
        if z % 9 == 0 and z >= max_s:
            max_s = max(max_s, z)
            r[max_s,x] = z//9

print(*r.items(),sep='\n')






