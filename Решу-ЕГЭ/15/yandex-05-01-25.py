B = {-42, -10, -8, 2, 16}
C = {-10, -4, 2, 15, 23}

A = set(range(100))

for x in range(1,100):
    if not (((x in A) <= (x in B)) or (x in C)):
        A.remove(x)

print(sum(A), A)
