# 791 75
f = open("я-март-25-10/26.txt")
f.readline()

balls = list(map(int, f.readline().split()))
print(balls)
children = []

for child in f:
    child = list(map(int, child.split()))
    children.append((list(x for x in child[1:]), child[0], sum(child[1:])))

children.sort(key=lambda x: (-x[2], x[1]))

students = {i: [] for i in range(5)}

while children:
    child = children.pop(0)
    c = 0
    for j, ball in enumerate(balls):
        if child[0][j] < ball:
            c += 1
    students[c].append(child)

print(students[0][-1][1])
print(students[4][0][1])

# 30396
# 20843
