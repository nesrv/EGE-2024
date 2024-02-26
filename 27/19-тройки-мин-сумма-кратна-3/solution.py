'''
4
5 2
8 15
7 14
11 9
'''

# f = open('27/19/txt.txt')
f = open('27/19/inf_26_04_21_27a.txt')
n = int(f.readline())
res = []
s1 = s2 = 0
for pair in f:
    a, b = (map(int, pair.split()))
    if a % 2 != 0:
        res.append(sorted((a, b), reverse=1))
 

res = sorted(res, key=lambda x: (x[0], x[1]), reverse=1)
lst_sum_max = [x[0] for x in res]
lst_sum_min = [x[1] for x in res]

print(lst_sum_max)
print(lst_sum_min)
sum_max = sum(lst_sum_max)
sum_min = sum(lst_sum_min)
i = 0
# print(res)
res = sorted(res, key=lambda x: (x[1], x[0]))
# print(res)
print(sum_max,sum_min )

while i < len(res):
    if sum_max % 2 != 0 and sum_min % 2 == 0:   
        print(sum_max,sum_min)
        break
    else:
        
        if (sum_max - res[i][0]) % 2 !=0 and (sum_min - res[i][1]) % 2 ==0:
            print(sum_max - res[i][0] ,sum_min - res[i][1])
            print(sum_max - res[i][0] + sum_min - res[i][1])
            break
    i+=1


# print(200772716)
# print(100880524)