A = 1
while True:
  OK = 1
  for x in range(0,1000):
    for y in range(0,1000):
      if not ((2*y + 4*x < A) or (x + 2*y > 80)):
        OK = 0
        break
    if not OK: break
  if OK:
    print(A)
    break
  A += 1