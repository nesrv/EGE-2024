from itertools import product

w = sorted('ВЕЧНОСТЬ')
s = 'ВЧНСТ'
words = product(w, repeat=6)

c = 0

for i, word in enumerate(words, 1):
    if i % 2 == 0 and word[0] not in s and word.count('О') >= 2:
        c += 1

print(c)
# 14509
