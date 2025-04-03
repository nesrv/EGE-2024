import re

# Читаем файл
with open("я-март-25-10/24.txt") as f:
    data = f.read()


# Создаем регулярное выражение для поиска пар "гласная + согласная"
pair_pattern = r'[AE][BCDF]'
pairs = re.findall(pair_pattern, data)

# Если пар меньше или равно 130, возвращаем длину всей строки
if len(pairs) <= 130:
    max_length = len(data)
else:
    # Используем скользящее окно
    max_length = 0
    left = 0
    current_pairs = 0
    
    for right in range(len(data)):
        # Если нашли новую пару
        if re.match(pair_pattern, data[right:right+2]):
            current_pairs += 1
            
        # Если превысили лимит пар, сдвигаем левую границу
        while current_pairs > 130:
            if re.match(pair_pattern, data[left:left+2]):
                current_pairs -= 1
            left += 1
            
        # Обновляем максимальную длину
        max_length = max(max_length, right - left + 1)

print(max_length)
