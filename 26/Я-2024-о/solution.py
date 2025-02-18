# правильно 264 7
f = open("26/Я-2024-о/txt-2.txt")
N,M,R = map(int, f.readline().split())

print("План =", 'st', 'rab', 'uni')
print("План =", N,M,R)
enter = [[] for _ in range(R+1)]
st_1 = []
counter = 0
for st in f:   
    student = list(map(int, st.split()))
    id_st, id_uni, score, status = student   
    if status == 1:
        enter[id_uni].append(student)
        counter += 1        
    else:
        st_1.append(student)
  
# print('Поступили в 1 очередь', *enter.items(), sep='\n', end='\n\n') 
# print('Ждут поступления', *st_1.items(), sep='\n', end='\n')

st_1.sort(reverse=True, key=lambda x: x[2])
# print(*st_1, sep='\n', end='\n' )
# забираем студентов по 2а критерию
for student in st_1:
    id_st, id_uni, score, status = student
    if not enter[id_uni]:      
        enter[id_uni].append(student)
        counter += 1
        st_1.remove(student)


# print('Поступили в 1+2 очередь', *enter.items(), sep='\n', end='\n') 
# print('Не поступили', st_1, sep='\n', end='\n')     

while counter < M:
    student = st_1.pop(0)
    id_st, id_uni, score, status = student
    enter[id_uni].append(student)
    counter += 1
 
 
# print('Поступили в 1+2+3 очередь', *enter.items(), sep='\n', end='\n')    
# рассчитать количество значение из enter с длиной списка 1
single_uni = len([i for i in enter if len(i) == 1])

print("Макс ID", st_1[0][0])
print("Единственные представители", single_uni)
