from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 1) * (n - 1)
    return f(n - 2) * (2 * n - 2)


for x in range(2,10048):
    f(x)

r = (f(10048) - f(10045))/f(10043)

print(r)