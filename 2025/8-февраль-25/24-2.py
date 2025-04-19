
from string import ascii_uppercase

data = open("24.txt", 'r').read()

for letter in ascii_uppercase:
    data = data.replace(letter, ' ')

data = data.split()
data = sorted(map(int, data))

print(data[-2:])