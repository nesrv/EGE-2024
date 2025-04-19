# 17-35
f = open("17/35.txt")

lst = [int(i) for i in f]
even = [int(i) for i in lst if (int(i) % 2)]
sr_even = sum(even) / len(even)

counter = max_s = 0

for i in range(len(lst)-1):
    if (lst[i] % 5 == 0 and lst[i+1] < sr_even) \
        or (lst[i+1] % 5 == 0 and lst[i] < sr_even):
        
        counter += 1
        max_s = max(max_s, lst[i] + lst[i+1])

print(counter, max_s) # 1061 14847
