# метод двух указателей

s = open("24/Яндекс-5/24.txt").readline()

m = u = t = l = 0


for r in range(len(s)):
    if s[r] == "T":
        t += 1
    if s[r] == "U":
        u += 1
    if t == 100 and u == 50:
        m = max(m, r - l + 1)
    
    while t > 100 or u > 50:
        if s[l] == "T":
            t -= 1
        if s[l] == "U":
            u -= 1
        l += 1
   
    
print(m)
