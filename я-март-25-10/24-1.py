from re import *

s = open("24.txt").read()


pairs = split(r"[AE][BCDF]", s)

max_length = 0

for i in range(len(pairs)):
    sequence = "".join(pairs[i:i+131])
    max_length = max(max_length, len(sequence))

print(max_length)