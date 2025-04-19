f = open("24/Яндекс-6/24 (13).txt").readline()

glas = "AEOU"
sogl = "KLMN"

c = 0
max_c = 0
for i in range(len(f)-1):
    if (f[i] in glas and f[i + 1] in sogl) or (f[i] in sogl and f[i + 1] in glas):
        c += 1
    else:
        max_c = max(max_c, c)
        c = 1
    
print(max_c) # 23
