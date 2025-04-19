
for A in range(1, 200):
    for x in range(1, 200):
        for y in range(1, 200):
            if not(((x >= A) or (121 >= x ** 2)) and ((y ** 2 < 49) or (A < y))):
                break
        else:
            continue
        break
    else:
        print(A)


print("-------")

for A in range(1, 100):
    c = 0
    for x in range(1, 101):
        for y in range(1, 101):
            if ((x >= A) or (121 >= x ** 2)) and ((y ** 2 < 49) or (A < y)):
                c += 1
                
    if c == 10_000:
        print(A)
        