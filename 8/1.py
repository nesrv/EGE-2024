c = 0
a = '12 21 32 23 25 52 27 72'.split()
alf = '012345678'
for x in alf:
    for y in alf:
        for z in alf:
            for w in alf:
                for q in alf:
                    A = x + y + z + w + q
                    if A.count('3') == 2 and A[0] != '0':
                        for e in a:
                            if e in A:
                                break
                        else:
                            c += 1
print(c)
