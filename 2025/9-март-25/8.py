from itertools import product

w = sorted('ВЕСНА')

words = product(w, repeat=5)

c = 0

for word in words:
    word = list(word)
    if word[0] == 'Н' and word.count('В') == 2:
        word.remove('В')
        word.remove('В')
        if len(word) == len(set(word)):
            c += 1

print(c)
