f = open("26/48 (конференция заявки)/48.txt")
n = int(f.readline())

lst = []

for i in f:
    x,y = map(int, i.split())
    lst.append((x,y))

lst.sort(key= lambda x : x[1])


users = [lst.pop(0)]

for i in lst:
    if i[0] >= users[-1][1]:
        users.append(i)

for user in lst:
    if user[0] <= users[-1][0] and user[0] >= users[-2][1]:
        users[-1] = user



print(len(users), users[-1][1])

