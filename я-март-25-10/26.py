# 791 75
f = open("26.txt")
f.readline()

balls = list(map(int, f.readline().split()))
print(balls)
all_users = []

for user in f:
    user = list(map(int, user.split()))
    all_users.append((list(x for x in user[1:]), user[0], sum(user[1:])))

all_users.sort(key=lambda x: (-x[2], x[1]))

students = {i: [] for i in range(5)}

while all_users:
    user = all_users.pop(0)
    c = 0
    for j, ball in enumerate(balls):
        if user[0][j] < ball:
            c += 1
    students[c].append(user)

print(students[0][-1][1])
print(students[4][0][1])

# 30396
# 20843
