#19-1
# def f1(s, n):
#     if n > 2:
#         return 0
#     if s >= 68 and n == 2:
#         return 1
#     s = f1(s + 1, n + 1), f1(s + 4, n + 1), f1(s * 5, n + 1)
#     return any(s)


# for s in range(1, 68):
#     if f(s, 0):
#         print(s)
#         break


#19-2

# def f2(s, n):
#     if s >= 68 or n > 3:
#         return n == 3
#     s = f2(s + 1, n + 1), f2(s + 4, n + 1), f2(s * 5, n + 1)
#     return all(s) if n == 1 else any(s)
#
#
# for s in range(1, 68):
#     if f2(s, 0):
#         print(s)


#19-3

def f2(s, n):
    if s >= 68 or n > 4:
        return n == 2 or n == 4
    s = f2(s + 1, n + 1), f2(s + 4, n + 1), f2(s * 5, n + 1)
    return all(s) if n == 0 or n == 2 else any(s)


for s in range(1, 68):
    if f2(s, 0):
        print(s)
