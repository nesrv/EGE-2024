f = open('40-Последовательность/27-B.txt')
count = 0

s = [int(x) for x in f]
for i in range(1, len(s)):
    for j in range(i, len(s)):
        if j - i  + 1 > 18:
            if (s[i] +s[j]) % 8 == 0 and (s[i]* s[j]) % 2187 == 0:
                count += 1

print(count)
