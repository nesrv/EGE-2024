# способ 6
ranges = range(13, 18), range(18, 31), range(31, 48), range(48, 80), range(81, 114)

P = range(13, 31)
Q = range(18, 80)
R = range(48, 114)

res = []

for A in ranges:      
      for x in range(1, 200):
          if ((not((x in Q) <= (x in P) or (x in R))) <= (not (x in A) <= (not (x in Q)))) == 0:
              break
      else:
          res.append(len(A))


print(min(res))

#


for left in range(0, 115):
    for right in range(left+1, 115):
        A = range(left, right)
        for x in range(1,115):
            if ((not ((x in Q) <= (x in P) or (x in R))) <= (not (x in A) <= (not (x in Q)))) == 0:
                break
        else:  
           res.append(right-left)

print(min(res))