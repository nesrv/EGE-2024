
from re import findall
s = open("досрок-2025/24_2.txt").read()

digits ='123456789AB'

max_x = 0
for i in range(len(s)-1):
    if s[i] in digits:
        for j in range(i+1, len(s)):
            if s[j] in digits:
               sub_s = s[i:j]
            else:
               x = int(sub_s, 12)
               if x % 6 == 0 and x > max_x:
                   max_x = x
                   res = x, sub_s
               break    


print (res)
                  
                  
    

