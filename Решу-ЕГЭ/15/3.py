points = 10, 29, 13, 18

P = set(range(10, 30))
Q = set(range(13, 19))

res = []
for a, b in zip(points[:-1], points[1:]):
    A = set(range(a, b + 1))
    for x in range(1, 101):
        if not (((x in A) <= (x in P)) or (x in Q)):
          break
    else:
        res.append(b - a)

print(max(res))
