f = open('from Polyakov/txt1.txt')
lst = [int(x) for x in f]
counter = 0
maxsum = 0
summ = 0
maxcount = 0
for i in range(1,len(lst) - 1):
    if lst[i] % lst[i-1] == 0 or lst[i] % lst[i+1] == 0:
        counter+=1
        summ += lst[i]
    else:
        if counter > maxcount:
            maxcount = counter
            maxsum = summ
        counter = 0
        summ = 0
print(maxcount,maxsum)