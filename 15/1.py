
P = set(range(5, 31))
Q = set(range(14, 24))

# способ 1
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


# способ 2
points = 5, 14, 23, 30


res = []
for startA in points:
    for endA in points:
        for x in points:
            if not ((5 < x < 30) == (14 < x < 23)) <= (not (startA <= x <= endA)):
                break
        else:
            res.append(endA-startA)

print(max(res))

# способ 3

res = []
for a, b in zip(points[:-1], points[1:]):
    A = set(range(a, b + 1))
    for x in range(1, 101):
        if not ((x in P) == (x in Q)) <= (not (x in A)):
            break
        else:
            res.append(b - a)
print(max(res))


# способ 4
res = []
for a, b in zip(points[:-1], points[1:]):
    A = set(range(a, b + 1))
    if not (P == Q) <= (not A):
        break
    else:
        res.append(b - a)
print(max(res))


# способ 5
res = []



for a, b in zip((5, 14, 23), (14, 23, 30)):
    A = set(range(a, b + 1))
    print(1, A)
    if (P == Q) <= (not A):
        res.append(b - a)
print(res)

# способ 6
ranges = range(5, 15), range(14, 24), range(23, 31)

P = set(range(5, 31))
Q = set(range(14, 24))
res = []
for range in ranges:
    A = set(range)
    print(2, A)
    if (P == Q) <= (not A):
        res.append(range)
    
print(res)


# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)

P = range(5, 30+1)
Q = range(14, 23+1)

l = set()

ranges = range(5, 15), range(14, 24), range(23, 31)
for A in ranges:
    for x in range(5, 31):
        if (((x in P) == (x in Q)) <= (not (x in A))) == 0:
            break
    else:
        l.add(A)

print(*l)
