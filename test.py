
s = 'aabcccccaaaacc'
# new_s = ''
# d = dict()
# for item in s:
#     if item in d:
#         d[item] += 1
#     else:
#         d[item] = 1

# res = ''.join(f'{key}{value}' for key, value in d.items())
# print(res)
new_s = ''
counter = 1
current= s[0]
for letter in s[1:]:
    if letter==current:
        counter+=1
    else:
        new_s+=f'{current}{counter}'
        current = letter
        counter=1
        
        

print(new_s)


