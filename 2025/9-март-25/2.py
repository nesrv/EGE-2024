from itertools import *
print ('x y z w f')
a = product((0, 1), repeat=4)
for x, y, z, w in a:
    f = ((z <= x) and ((not y) and ((not w) == y )))
    print (y, x, w, z, f)


'''

0 1 1 0 True
0 1 1 1 True


0 1 0 0 False
1 0 0 0 False


1 0 0 1 False


1 1 0 0 False
1 1 0 1 False

'''