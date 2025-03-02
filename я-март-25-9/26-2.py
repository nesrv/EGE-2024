
f = open('26.txt', 'r')
M, P = map(int, f.readline().split())
requests = [tuple(map(int, line.split())) for line in f]

# Сортируем запросы по времени поступления (и длительности для одинаковых минут)
requests.sort(key=lambda x: (-x[1], x[0]))

printers = [0] * M  # время освобождения каждого принтера

# Переменные для отслеживания результатов
delay_count = 0
last_non_delayed = 0

# Обрабатываем каждый запрос
for start, duration in requests:
    # Ищем первый свободный принтер
    printer_index = None
    for i in range(M):
        if printers[i] + 3<= start:
            printer_index = i
            break

    # Если все принтеры заняты
    if printer_index is None:
        delay_count += 1
        # Выбираем принтер, который освободится раньше
        printer_index = min(range(M), key=lambda i: printers[i])

    # Вычисляем время начала печати
    start_time = max(start, printers[printer_index])

    # Обновляем время освобождения принтера
    printers[printer_index] = start_time + duration + 3  # +3 минуты на обслуживание

    # Обновляем время последнего незадержанного запроса
    if start_time == start:
        last_non_delayed = max(last_non_delayed, start_time + duration)




print(f"Количество запросов с задержкой: {delay_count}")
print(f"Минута завершения последнего незадержанного запроса: {last_non_delayed}")


# 791 75