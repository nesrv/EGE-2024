from itertools import *


stop_list = "02 04 06 20 24 26 40 42 46 60 62 64 66 35 37 53 57 73 75".split()

c = 0
for x in permutations('0234567', 5):
    x = ''.join(x)
    if x[0] != '0':   
      for stop in stop_list:
          if stop in x:
              break
      else:
          c+=1

print(c)            
            
        
# x = '20000'
# y = int(x, 8)
# print(y)
