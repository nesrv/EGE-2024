# При каком наибольшем целом A найдутся
# такие целые неотрицательные x и y, что выражение

# (3x + y > 48)∨(x > y)∨(4x + y < A)

# будет ложным?


for a in range(100, 1, -1):
    for x in range(0, 100):
        for y in range(0, 100):
            if ((3 * x + y > 48) or (x > y) or (4 * x + y < a)) == False:
                print(a)
                exit()
