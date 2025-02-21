# 4229

f = open("26/статград/stat-71.txt")
len_all = f.readline()
all = [list(map(int,s.split())) for s in f]
for user in all:
  
    without_negative = sum(filter(lambda x: x > 0, user[1:]))
    without_zero = len(list((filter(lambda x: x != 0, user[1:]))))
    user.extend((sum(user[1:]),without_negative, without_zero) )

# for i in range(len(all)):
#     without_negative = sum(filter(lambda x: x > 0, all[i][1:]))
#     without_zero = len(list((filter(lambda x: x != 0, all[i][1:]))))
#     all[i].extend((sum(all[i][1:]),without_negative, without_zero) )
  
all.sort(key=lambda x: (-x[-3], -x[-2], -x[-1], x[0]))    
# взять третью часть от всех данных
slice = len(all) // 3 + 20
all_30 = all[:slice]

print(*all_30, sep='\n')

# посмотреть после 
print('=' * 20)
print(*all[slice:slice+20], sep='\n')

print('=' * 20)

user_1500 = all[1500]
count_same_1500 = filter(lambda x: x[-3:] == user_1500[-3:], all)
print(user_1500)
print(len(list(count_same_1500)))