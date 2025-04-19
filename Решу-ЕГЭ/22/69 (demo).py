f = open("22/69.txt")

processes = {}

for s in f:
    idB, t, *idA = map(int, s.split())
    if idA[0] == 0:
        processes[idB] = 0, t
    elif len(idA) > 1:
        max_t = max(processes[idA[0]][1], processes[idA[1]][1])
        processes[idB] = max_t, max_t + t
    elif len(idA) == 1:
        processes[idB] = processes[idA[0]][1], processes[idA[0]][1] + t


processes = dict(sorted(processes.items(), key=lambda x: x[1][0]))


# в течение которого возможно одновременное выполнение максимального количества процессов
# during which the maximum number of processes can be executed simultaneously?

print(*processes.items(), sep="\n")


events = []
for process_id, (start, end) in processes.items():
    events.append((start, 1))  # 1 for process start
    events.append((end, -1))   # -1 for process end

# Sort events by time
events.sort()
print(events)


# current_processes = 0
# max_processes = 0
# max_time = 0

# # Find the time with maximum concurrent processes
# for time, event_type in events:
#     current_processes += event_type
#     if current_processes > max_processes:
#         max_processes = current_processes
#         max_time = time

# print(f"Maximum number of concurrent processes: {max_processes}")
# print(f"Time when maximum is reached: {max_time}")
