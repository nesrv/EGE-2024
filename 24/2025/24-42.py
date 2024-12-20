from collections import Counter

# s = '''
# ABBAAABBABBXY
# XYAYYXYABA
# '''.split()

s = open("24.txt").readlines()


res = []
for sub_s in s:
    temp = ''
    for i in range(len(sub_s) - 1):
        if sub_s[i] == 'A':
            temp += sub_s[i + 1]
    counter = Counter(temp).most_common()

    max_count = counter[0][1]
    res += [value for value, count in counter if count == max_count]

print(Counter(res))

