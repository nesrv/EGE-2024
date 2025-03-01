from itertools import *
print ('x y z w')
a = product((0, 1), repeat=4)
for x, y, z, w in a:
    print(w, z, x, y, ((x == (y <= z)) and (y == (not (z <= w)))))

'''
0 0 1 0 True
1 0 1 0 True
1 0 1 1 False


1 1 0 0 False
1 0 0 1 False

1 1 0 1 False


'''