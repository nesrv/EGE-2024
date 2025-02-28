# 172602369 1
# 176802369 2
# 1700002389 1
# 1725402339 7
# 1767602349 1


from fnmatch import fnmatch


prime_numbers = set()
for x in range(2, 100_000):
    for y in range(2, int(x**0.5)+1):
        if x % y == 0:
            break
    else:
        prime_numbers.add(x)

def check_sum(x):
    s = 0
    for d in prime_numbers:
        if x % d == 0:
            s+=d    
    return s

result = []

mask = '17*023?9'
#       1702319

for num in range(1702309, 10**10 + 1):   
    if fnmatch(str(num), mask):       
        if check_sum(num) % 1304 == 0:
            result.append(num)
            print(num)
            if len(result) == 5:
                break
print(result)