# Тип 21 № 58529 (34 или 33)
#  В игре, описанной в задании 19, в начальный момент в первой куче был 31 камень, а во второй S камней, 1 <= S <=  39.
# # Найдите такое значение S, при котором у Вани есть стратегия, позволяющая ему выиграть вторым ходом 
# при любой игре Пети, но у Вани нет стратегии, которая позволяла бы ему гарантированно выиграть первым ходом.

def f(x, y, n):
    if x >= 40 or y >= 40 or n > 4:
        return n == 4 or n == 2 # негарантированная победа В-1 (нужно проверять по условию)
    if n % 2 != 0:
        if x > y:
            return (f(x + 1, y, n + 1)
                    or f(x + 2, y, n + 1)
                    or f(x + 3, y, n + 1)
                    or f(x, y * 2, n + 1))
        elif y > x:
            return (f(x, y + 1, n + 1)
                    or f(x, y + 2, n + 1)
                    or f(x, y + 3, n + 1)
                    or f(x * 2, y, n + 1))
        else:
            return (f(x + 1, y, n + 1)
                    or f(x + 2, y, n + 1)
                    or f(x + 3, y, n + 1)
                    or f(x, y + 1, n + 1)
                    or f(x, y + 2, n + 1)
                    or f(x, y + 3, n + 1))
    else:
        if x > y:
            return (f(x + 1, y, n + 1)
                    and f(x + 2, y, n + 1)
                    and f(x + 3, y, n + 1)
                    and f(x, y * 2, n + 1))
        elif y > x:
            return (f(x, y + 1, n + 1)
                    and f(x, y + 2, n + 1)
                    and f(x, y + 3, n + 1)
                    and f(x * 2, y, n + 1))
        else:
            return (f(x + 1, y, n + 1)
                    and f(x + 2, y, n + 1)
                    and f(x + 3, y, n + 1)
                    and f(x, y + 1, n + 1)
                    and f(x, y + 2, n + 1)
                    and f(x, y + 3, n + 1))


s = set()
for x in range(1, 40):
    if f(31, x, 0):
        s.add(x)

print(s)
