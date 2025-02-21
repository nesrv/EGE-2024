# 4217 298
# 8 февраль 2025
# В палату мер и весов поступил набор из N гирек. 

# f = open("26/Я-2025-Ф-8/txt.txt")
f = open("26/Я-2025-Ф-8/26.txt")
n = int(f.readline())

w = [int(x) for x in f]

w.sort()
sum_w  = sum(w)
targets = set()
c = 1
def subset_sum(numbers, target,  partial=[]):
    s = sum(partial) 
    global c  
    if s == target ==c:      
        # print(target, c, partial)        
        c+=1        
    if s >= target or target>c:
        return 

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        if target not in targets:
            subset_sum(remaining, target,  partial + [n])



for s in range(1, sum_w):  
    subset_sum(w, s )

print(c)