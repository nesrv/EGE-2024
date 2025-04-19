def solve_printing_problem(filename):
    # Считываем данные из файла
    with open(filename) as f:
        M, P = map(int, f.readline().split())
        requests = [tuple(map(int, line.split())) for line in f]

    # Сортируем запросы по времени поступления (и длительности для одинаковых минут)
    requests.sort(key=lambda x: (-x[1], x[0]))

    # Инициализируем принтеры
    printers = [0] * M  # время освобождения каждого принтера

    # Переменные для отслеживания результатов
    delay_count = 0
    last_free_completion = 0

    # Обрабатываем каждый запрос
    for arrival, duration in requests:
        # Находим первый доступный принтер
        printer_index = min(range(M), key=lambda i: printers[i])

        # Если принтер свободен в момент поступления запроса
        if printers[printer_index] <= arrival:
            # Запускаем печать без задержки
            printers[printer_index] = arrival + duration + 3  # +3 минуты на обслуживание
            last_free_completion = max(last_free_completion, printers[printer_index])
        else:
            # Запрос выполняется с задержкой
            delay_count += 1
            # Рассчитываем новое время завершения
            printers[printer_index] = printers[printer_index] + duration + 3

    return delay_count, last_free_completion


# Пример использования
filename = "26.txt"
delays, last_free = solve_printing_problem(filename)
print(f"Количество запросов с задержкой: {delays}")
print(f"Время завершения последнего запроса без задержки: {last_free}")