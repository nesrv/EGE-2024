# 9
def f3(x):
    s = ''
    while x:
        x,y = divmod(x, 3)
        s += str(y)
    return s[::-1]

mapping = {'0': '1', '1': '2', '2': '0'}


for N in range(1, 20):
    R = f3(N)
    if N % 3:
        R = (mapping[digit] for digit in R)
    R = ''.join(digit * 2 for digit in R)
    R  = int(R, 3)
    if R > 120:
        print(N)
        break




