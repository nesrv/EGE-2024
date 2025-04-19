B = range(74,194)
C = range(152,223)
lst = []

for t1 in range(74,223):
    for t2 in range(t1+1,224):
        A = range(t1,t2)
        for x in range(74, 224):
            if ((not(x in A) and (x in B)) <= ((x in B) <= (not (x in C)))) == 0:
                break
        else:
            lst.append(len(A))

print(min(lst))        # 42


# from itertools import combinations

# ox = range(74, 224)
# res = []
# for t1,t2 in combinations(ox, 2):
#   ...
