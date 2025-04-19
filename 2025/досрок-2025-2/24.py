from re import findall
s = open("досрок-2025-2/24_21421.txt").read()

t = '[1-9AB]{1}[0-9AB]{18}'


res = findall(t, s)

for x in res: 
    y = int(x, 12)
    if y % 2 == 0:
        print(x, y, len(x))

