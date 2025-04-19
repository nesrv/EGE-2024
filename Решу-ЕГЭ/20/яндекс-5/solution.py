# https://education.yandex.ru/ege/variants/7abf7990-4043-4fe4-b5ce-bcc69d714df9/task/20

def f(s, n, h):
    if s >= 131 or n > 4:
        return n == 4 or n == 2
    if n == 0:
        return f(s+2, n+1, "+2") and f(s+1, n+1, "+3") and f(s*2, n+1, "*2")
    if n == 1 or n == 3:
        if h == "+2":
            return f(s+3, n+1, "+3") or f(s*2, n+1, "*2")
        if h == "+3":
            return f(s+2, n+1, "+2") or f(s*2, n+1, "*2")
        if h == "*2":
            return f(s+2, n+1, "+2") or f(s+3, n+1, "+3")
    if n == 2 or n == 4:
        if h == "+2":
            return f(s+3, n+1, "+3") and f(s*2, n+1, "*2")
        if h == "+3":
            return f(s+2, n+1, "+2") and f(s*2, n+1, "*2")
        if h == "*2":
            return f(s+2, n+1, "+2") and f(s+3, n+1, "+3")


for s in range(1, 131):
    if f(s, 0, ""):
        print(s)
