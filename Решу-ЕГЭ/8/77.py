from itertools import *
from itertools import product


s = "КОМПЬЮТЕР"

s = "ЕКМОПРТЬ"

words = product(s, repeat=5)


for i,word in enumerate(words,1):
    w = "".join(word)
    if w.count("К") <= 1 and w.count("Р") == 2:
        print(i,w)
