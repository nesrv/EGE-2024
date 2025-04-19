
for A in range(1,129):
    for x in range(1, 129):
        if not ((x | 42 > 64) and (x | 34 <= 102)) <= (not (x | A < 70)):
            break
    else:
        print(A)
        break