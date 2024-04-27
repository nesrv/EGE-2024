f = open('26/31 (unix время)/26.txt')

n = f.readline()

start_time = 1_634_515_200
week = 7 * 24 * 3_600
end_time = start_time + week
counter = 0
process = []

for times in f:
    start_process, end_process = map(int, times.split())
    if start_process <= start_time and (end_process >= start_time or end_process == 0):
        counter = counter + 1
    elif start_process >= start_time and end_process <= end_time:
        process.append(
            (start_process, end_time if end_process == 0 else end_process))

# sum_time = 0
# max_process = 0
# process.sort()
# print(process[:10])
c = 0
max_counter = 0
i = 0
print(len(process))
exit()
while i < len(process)-1:
    current = process[i]
    j = i + 1
    print(i,j)
    while current[1] <= process[j][0]:
        c += 1
        j += 1
    max_counter = max(max_counter, counter + c)
    c -= 1
    i += 1


print(max_counter)
