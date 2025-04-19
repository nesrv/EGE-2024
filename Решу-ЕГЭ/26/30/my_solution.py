f = open('26/31 (unix время)/26.txt')

n = f.readline()

start_time = 1_634_515_200
week = 7 * 24 * 3_600
end_time = start_time + week
counter = 0
process = [0] * week

for times in f:
    start_process, end_process = map(int,times.split())
    if start_process <= start_time and (end_process >= start_time or end_process == 0):
        counter = counter + 1
    
    if  start_time <= start_process <= end_time:
        process[start_process - start_time] = process[start_process - start_time] + 1
    
    if end_process >= start_time and end_process <= end_time:
        process[end_process - start_time] = process[end_process - start_time] - 1

sum_time = 0
max_process = 0

for sec in range(week):
    counter = counter + process[sec]
    if counter > max_process:
        max_process = counter
    #     sum_time = 0
    # if counter == max_process:
    #     sum_time = sum_time + 1

print(max_process, sum_time)
