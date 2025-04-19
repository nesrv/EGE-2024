# способ 1
points = 25,32,47,50

P = set(range(25, 51))
Q = set(range(32, 48))

res = []
for a, b in zip(points[:-1], points[1:]):
    A = set(range(a, b + 1))
    for x in range(1,101):
        if not ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q)):
          break
    else:
        res.append(b - a)

print(max(res))

# способ 2 не работает
res = []
for a, b in zip(points[:-1], points[1:]):
    A = set(range(a, b + 1))    
    if not (((not  A) <=  P) <=  (A <=  Q)):
          res.append(b - a)

print(max(res))
