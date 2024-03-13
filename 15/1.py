P = set(range(5, 31))
Q = set(range(14, 24))

res = []
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        A = range(Amin, Amax)
        for x in range(1, 101):
            if not ((x in P) == (x in Q)) <= (not (x in A)):
                break
        else:
            res.append(Amax - Amin)
print(max(res))

points = 5, 14, 23, 30
maxA = 0

res = []
for startA in points:
    for endA in points:
        for x in points:
            if not ((5 < x < 30) == (14 < x < 23)) <= (not (startA <= x <= endA)):
                break
        else:
            res.append(endA-startA)

print(max(res))

P = set(range(5, 31))
Q = set(range(14, 24))
res = []
for a, b in zip(points[:-1], points[1:]):
    A = set(range(a, b + 1))
    for x in range(1,101):
        if not ((x in P) == (x in Q)) <= (not (x in A)):
            break
        else:
            res.append(b - a)
print(max(res))


P = set(range(5, 31))
Q = set(range(14, 24))
res = []
for a, b in zip(points[:-1], points[1:]):
    A = set(range(a, b + 1))
    if not (P == Q) <= (not A):
        break
    else:
        res.append(b - a)
print(max(res))
