
def f(n):
    if n >= 2024:
        return 1
    else:
        return f(n + 2) + f(n + 4)

s = []
for x in range(2024,2003,-1):
    s.append((x,f(x)))
    
print(*s, sep='\n') # последовательност Фибоначчи

print('ответ - ', 2024//2 + 1) 

