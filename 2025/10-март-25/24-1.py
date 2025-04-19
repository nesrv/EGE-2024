from re import *

s = open("я-март-25-10/24.txt").read()


s = s.replace('A', 'A ').replace('E', 'E ')
s = s.replace('B', ' B').replace('C', ' C')
s = s.replace('D', ' D').replace('F', ' F')
pairs = s.split()


# pairs = split(r"[AE][BCDF]", s)




max_length = 0

for i in range(len(pairs)):
    sequence = "".join(pairs[i:i+131])
    max_length = max(max_length, len(sequence))

print(max_length)

# 645