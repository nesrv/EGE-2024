for A in range(1,100):
    c = 0
    for x in range(1, 101):
        for y in range(1, 101):
            if ((5 < y) or (x > 32) or (x + 2 * y < A)):
                c+=1
    if c == 10_000:
        print(A)
        break    
       