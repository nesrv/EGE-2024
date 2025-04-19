s = '''
ABBAAABBABBXY
XYYYXYAB
'''.split()


s = open('24/2025/24 (1).txt')

# Найти самую длинную цепочку из одиннаковых символов
max_c = 0 # сколько раз встречается буква
current_len = 0 # длина самой длиной цепочкой с этой буквой
c = 0
for sub_s in s:   
    for i in range(len(sub_s) - 1):
        if sub_s[i] == sub_s[i + 1]:
            c += 1
            if c > current_len:
                current_len = c
                max_c = sub_s.count(sub_s[i])
            if c == current_len:
                max_c = max(max_c, sub_s.count(sub_s[i]))
        else:           
            c = 1

print(max_c)
              
    



