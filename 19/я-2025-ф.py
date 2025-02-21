# Петя и Ваня устали перекладывать камни и собрали игровой автомат.
# 80
# 62 3
# 77

# 18

def f(s1, s2, n):
    if s1 + s2 >= 180 or n > 2:
        return n == 2
    h = (
        f(s1+2, s2, n + 1),
        f(s1, s2+2, n + 1),
        f(s1+s2, s2, n + 1),
        f(s1, s1+s2, n + 1),
    )
    return any(h) if n == 1 else all(h)


for s2 in range(1, 100):
    if f(18, s2, 0):
        print(s2)
        break

print ('----20-----')

def f(s1, s2, n):
    if s1 + s2 >= 180 or n > 3:
        return n == 3
    h = (
        f(s1+2, s2, n + 1),
        f(s1, s2+2, n + 1),
        f(s1+s2, s2, n + 1),
        f(s1, s1+s2, n + 1),
    )
    return any(h) if n % 2 ==0 else all(h)


for s2 in range(1, 100):
    if f(18, s2, 0):
        print(s2)
       
print ('----21-----')

def f(s1, s2, n):
    if s1 + s2 >= 180 or n > 4:
        return n == 2 or n == 4
    h = (
        f(s1+2, s2, n + 1),
        f(s1, s2+2, n + 1),
        f(s1+s2, s2, n + 1),
        f(s1, s1+s2, n + 1),
    )
    return any(h) if n % 2  else all(h)


for s2 in range(1, 100):
    if f(18, s2, 0):
        print(s2)
        break
       
