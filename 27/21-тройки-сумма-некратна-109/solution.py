# f = open('27/21/txt.txt')
f = open('27/21/27_B.txt')

'''
1 3 7
5 12 6
6 9 11
5 4 8
3 5 4
1 1 1
'''

n = int(f.readline())
total_sum = 0

min_dif = 10**5
for line in f:
    a, b, c = sorted(map(int, line.split()))
    total_sum += c
    if (c - a)  % 109 != 0:        
        min_dif = min(min_dif, c-a)
    if (c - b)  % 109 != 0:       
        min_dif = min(min_dif, c-b)


print(total_sum - min_dif)
