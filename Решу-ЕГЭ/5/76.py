sp = [0] * 1000
for n in range(1,49):
    r = f'{n:b}'
    r += f'{n%4:b}'
    r = int(r,2)
    sp[r] = 1
mch = 0
for i in range(1000):
    mch = max(mch, sum(sp[i : i + 49]))
print(mch)