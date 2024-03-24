def ТРЕУГ(a, b, c):
    return a < b + c and b < a + c and c < a + b


for A in range(1, 400):
    for x in range(1, 400):
        if ((ТРЕУГ(x, 10, 20) <= 
             (not (max(x, 8) > 24))) == 
             (not (ТРЕУГ(3, A, x)))) == False:
            break
    else:
        print(A)
