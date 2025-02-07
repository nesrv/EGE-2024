
s = set()

for x in range(190):
    for y in range(190):
        A = 23 * 190 ** 2 + x * 190 ** 1 + 32 
        B = 34 * 190 ** 3 + y * 190 ** 2 + 10 * 190 + 34
        if (A + B) % 189 == 0:
            s.add((x*y, (A+B)//189))
        


print(max(s))
    