# Тип 19 № 63068
# https://inf-ege.sdamgia.ru/problem?id=63068

def f(s, n):
    if s >= 132 or n > 2:
        return n == 2
    if n == 1:
      return f(s + 1, n + 1) or f(s * 3/2, n + 1) if s % 2 == 0 else 0 \
          or f(s * 4 // 3, n + 1) if s % 3 == 0 else 0\
          or f(s * 2, n + 1) if s % 3 != 0 and s % 2 != 0 else 0
    else:
        return f(s + 1, n + 1) and f(s * 3/2, n + 1) if s % 2 == 0 else 0 \
            and f(s * 4 // 3, n + 1) if s % 3 == 0 else 0\
            and f(s * 2, n + 1) if s % 3 != 0 and s % 2 != 0 else 0

for s in range(1, 68):
    if f(s, 0):
        print(s)
