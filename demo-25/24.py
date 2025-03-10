from re import *

from re import findall

# s = '7-99*00-00--88-*00*80*06---7'
f = open("demo_2025_24.txt")
s = f.read()

# Создаем регулярное выражение для корректных выражений
# (?:0|[6-9][0-9]*) - число без ведущих нулей
# (?:[-*]) - операция

# pattern = r'(?:0|[1-9][0-9]*)(?:[-*](?:0|[1-9][0-9]*))*'


pattern = r'[1-9][0-9]*([-*]+[1-9][0-9]*)*'

matches = findall(pattern, s)

max_length = max(matches , key=len)

print(len(max_length)  )