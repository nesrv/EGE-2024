from itertools import *
from itertools import permutations
word = "ВОЗДУХ"

stop = 'ОВ', 'ВО', 'ОХ', 'ХО', 'УВ', 'УВ', 'УХ', 'ХУ'

print(*stop)


def f(word):    
    for st in stop:
        if st in word:
            return False
    return True


c = 0

for x in product(word, repeat=5):
    x = ''.join(x)
    if ((x.count("У") == 1 and f(x)) ^ (x.count("О")==1 and f(x))) :
        c+=1
        print(x)
        
print(c)

# 896