from itertools import *

s = open("24.txt").read()


pairs = [''.join(pair) for pair in product('AE', 'BCDF')]


for pair in pairs:
    s = s.replace(pair, pair[0] + " " + pair[1])

parts = s.split()

max_length = 0
for i in range(len(parts)):
    sequence = "".join(parts[i:i+131])
    max_length = max(max_length, len(sequence))

print(max_length)