f = open('26/49 (конференция заявки)/26.txt')
n = int(f.readline())

all_users = [list(map(int, i.split())) for i in f]
all_users.sort(key=lambda x: x[1])


users = [all_users[0]]

for time in all_users:
    if time[0] >= users[-1][1]:
        users.append(time)

last_user = users[-1]
pre_last_user = users[-2]

for time in all_users:
    if time[0] > last_user[0]:
        last_user = time
    

print(len(users), last_user[0] - pre_last_user[1])
