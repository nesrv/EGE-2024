num = int(625 ** 90) + int(125 ** 120) - 5 * 25 
s = '' 
even_sum = 0
while num > 0: 
    ost = num % 25
    if ost % 2 == 0:
        even_sum += ost    
    num //= 25 



print(even_sum)