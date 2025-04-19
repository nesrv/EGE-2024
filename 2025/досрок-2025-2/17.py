f = open("досрок-2025-2/17_21416.txt")

lst = [int(x) for x in f]

sum_negatives = sum(x for x in lst if x < 0)


c = 0
max_sum = 0

for i in range(len(lst)-2):
    trio = lst[i : i + 3]
    max_x = max(trio)
    min_x = min(trio)
    if max_x * min_x > sum_negatives:
        c += 1
        max_sum = max(max_sum, sum(trio))
        
print(c, max_sum)


# ! 10007 7953