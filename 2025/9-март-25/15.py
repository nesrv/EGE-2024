
P = {x for x in range(1, 100) if x % 5 == 0}
Q = {x for x in range(1, 100) if x % 3 == 0}

A = list(range(1,100))

for x in A:
    if not (( x in Q ) <= ((x in P) <= ((x in Q) and (x in A)))):
        A.remove(x)

print(A)