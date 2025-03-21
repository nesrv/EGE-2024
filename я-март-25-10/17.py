f = open("17.txt")
data = [int(line) for line in f]
max_36 = max(num for num in data if num % 36 == 0)

c = 0
min_s = 10 ** 10


def end36(x):
    return x > 0 or abs(x) % 100 == 36

for i in range(len(data)-2):
    x,y,z = data[i:i+3]
    if end36(x) + end36(y) + end36(z) >= 2 and x + y + z <= max_36:
        c += 1
        min_s = min(min_s, x + y + z)

print(c, min_s)

# 3457
# -175325
