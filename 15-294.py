A = 100
while True:
  OK = 1
  for x in range(1,1000):
    for y in range(1,1000):
      if not ((y+4*x<A) or (x+3*y>100) or (5*x+2*y>152)):
        OK = 0
        break
    if not OK: break
  if OK:
    print(A)
    break
  A += 1