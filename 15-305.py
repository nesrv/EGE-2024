A = set(range(30, 50+1))
B = set(range(40, 46+1))

def f(x):
  return ((x not in B) <= (x not in A)) and \
         ((x not in C) <= (x in B))

for N in range(1, 100):
  C = set(range(N, 61+1))
  count = 0
  for x in range(100):
    if f(x):
      count += 1
      #print(count, x)
  if count > 25:
    print(N)



