x = 7 * 49**120 - 6 * 343**65 - 5 * 7**40

c = 0
while x:
    x, ost = divmod(x, 7)
    if ost == 6:
        c += 1


print(c)
