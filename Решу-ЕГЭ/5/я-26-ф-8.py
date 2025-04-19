def f3(x):
    s = ''
    while x:
        x, ost = divmod(x, 3)
        s = str(ost) + s
    return s if s else '0'


N_MAX = 0

for N in range(1, 100):
    R = f3(N)
    c2 = R.count('2')
    c2 = f3(c2)
    R += c2
    c1 = R.count('1')
    c1 = f3(c1)
    R += c1
    c0 = R.count('0')
    c0 = f3(c0)
    R += c0
    R = int(R, 3)
    if R <=1000:
        N_MAX = max(N_MAX, N)


print(N_MAX)

