

for A in range(1,128):
    for x in range(1, 128):
        if not ((x & 91 == 0) or ((x & 77 == 0) <= ((x & A) != 0))):
            break
    else:
        print(A)