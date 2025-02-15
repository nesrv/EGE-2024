# 621 170155300
f = open("25/Я-2025-Я-7/txt.txt")
L, P, N = map(int, f.readline().split())
print(L, P, N)
lots = {x: [] for x in range(0, L)}

for lot in f:
    lot = lot.split() 
    lots[int(lot[0])].append(int(lot[2]))
    lots[int(lot[0])].sort()
    if len(lots[int(lot[0])]) > 2:
        lots[int(lot[0])].pop(0)
    


lots = {k: min(v) for k, v in lots.items() if len(v) == 2}
# найти сумму всех лотов

print(sum(lots.values()))
print(len(lots))

