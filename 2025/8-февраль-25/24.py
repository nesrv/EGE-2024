import re


data = open("24.txt", 'r').read()

numbers = re.findall(r'[0-9]+', data)

even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
#
result = max(even_numbers)

print(f"Максимальное чётное число: {result}")