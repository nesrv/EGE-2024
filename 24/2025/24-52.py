s = 'BADCBACKLMENBCAAA'
s = open("24/2025/24 (2).txt").read()

set_s = set('ABC')
res = []

for i in range(len(s)-2):
    sub_s = s[i:i+3]
    if set(sub_s) == set_s:   
        res.append(i)


res = [res[i+1]-res[i] for i in range(len(res)-1)]
print(max(res)-3)
    



