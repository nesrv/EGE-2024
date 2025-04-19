f = open('26/50 (конференция заявки)/26_59776.txt')
n = int(f.readline())

all_users = []
for time in f:
    t1, t2 = map(int, time.split())
    all_users.append((t1, t1+t2))

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

