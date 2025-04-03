# 19

# def f1(s1, s2, n):
#     if s1 + s2 >= 189 or n > 2:
#         return n == 2
#     h = (
#         f1(s1 + s2, s2, n + 1),
#         f1(s1, s2 + s1, n + 1),
#         f1(s2, s2, n + 1) if s1 > s2 else f1(s1, s1, n + 1),
#     )
#     return any(h)


# for i in range(1, 189):
#     if f1(5, i, 0):
#         print(i)
#         break


# 20

def f2(s1, s2, n):
    print(s1,s2, n)
    if s1 + s2 >= 189 or n > 3:
        return n == 3
    h = (
        f2(s1 + s2, s2, n + 1),
        f2(s1, s2 + s1, n + 1),
        f2(s2, s2, n + 1) if s1 > s2 else f2(s1, s1, n + 1),
    )
    return any(h) if n % 2==0 else all(h)


for s2 in range(1, 183):
    if f2(5, s2, 0):
        print(s2)
        
print('___________')