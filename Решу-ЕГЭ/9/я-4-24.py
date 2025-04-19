f = open("9/9-2.txt")

c = 0
for str in f:
    m = list(map(int, str.split(",")))
    m.sort()
    p = [x for x in m if m.count(x) == 3]
    n = [x for x in m if m.count(x) == 1]
    sum_m1 = sum(1 for x in m if x % 2)
    sum_m2 = sum(1 for x in m if x % 2 == 0)
    sum_max = sum(m[-2:]) >= sum(m[:-2]) * 2
    print(sum_m1, sum_m2, sum_max)
    # if len(p) == 3 and len(n) == 3 and sum_m2 > sum_m1 and sum_max:
    #     c += 1

print(c)
