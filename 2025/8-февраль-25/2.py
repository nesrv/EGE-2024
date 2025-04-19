from itertools import product

print("x y w")
for x, y,  w in product((0, 1), repeat=3):
    f = ((x <= y) and 1)
    print(w, x, y, f)



'''

x y w
0 1 0 False
1 1 0 False
1 0 1 1
1 1 1 1

0 0 0 1
1 0 0 1
0 0 1 1

0 1 1 1





'''