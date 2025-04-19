def summ(n):
    sumi = 0
    while n:
        sumi += n % 10
        n = n // 10
    return str(sumi % 2)


A = 123_456_789
B = 1_987_654_321
counter = 0
for N in range(1, 20):
    print(bin(N)[2:], end='-')
    for _ in range(3):
        R = f'{N:b}'
        R += summ(N)
        N = int(R, 2)
    print(bin(N)[2:])

print(counter)
print((B-A)//8)


def f(n):
    for i in range(3):
        n = 2*n + sum(map(int,str(n)))%2
    return n

a,b = 123456789,1987654321
n = a // 8
m = b // 8
# while f(n) < a:
#     n += 1
# while f(m) <= b:
#     m += 1

print(m-n)