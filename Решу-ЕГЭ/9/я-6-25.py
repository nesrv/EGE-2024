f = open("9/9-1.txt")

c = 0
for str in f:
    str = str.split(";")
    if float(str[1]) - float(str[2]) >= 5 and (
        float(str[5]) in range(0, 46) or float(str[5]) in range(315, 361)
    ):
        c+=1
        
print(c)
