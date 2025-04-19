# 19
print("======19====== ")
def f(s1, s2, n):
    if s1 + s2 >= 143 or n > 2:
        return n == 2
    s = [f(s1+3, s2, n+1), f(s1*2, s2, n+1),f(s1, s2+3, n+1), f(s1, s2*2, n+1)]
    return any(s)


for s2 in range(1, 124):
    if f(16, s2, 0):
        print("19 = ", s2)
        break


# 20
def f(s1, s2, n):
    if s1 + s2 >= 143 or n > 3:
        return n == 3
    s = [f(s1+3, s2, n+1), f(s1*2, s2, n+1),f(s1, s2+3, n+1), f(s1, s2*2, n+1)]
    return any(s) if n % 2==0 else all(s)

print("======20====== ")
for s2 in range(1, 124):
    if f(16, s2, 0):
        print(s2)
    

# 21
def f(s1, s2, n):
    if s1 + s2 >= 143 or n > 4:
        return n == 4 or n == 2
    s = [f(s1+3, s2, n+1), f(s1*2, s2, n+1),f(s1, s2+3, n+1), f(s1, s2*2, n+1)]
    return any(s) if n % 2== 1 else all(s)

print("==========21========== ")
for s2 in range(1, 124):
    if f(16, s2, 0):
        print(s2)