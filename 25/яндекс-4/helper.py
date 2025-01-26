x = 731021

sqrt_x = int(x ** 0.5)

for i in range(sqrt_x-8,  sqrt_x + 8):
    if x % i == 0:
        print(i)
