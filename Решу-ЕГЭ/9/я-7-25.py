f = open("9.txt")

all_string = f.readlines()
lst = []
c = 0
for string in all_string:
    string = sorted(map(int, string.split(';')))
    res = sum(string[1:-1]) / len(string[1:-1])
    if res >= 8:
        c += 1

print(c)
