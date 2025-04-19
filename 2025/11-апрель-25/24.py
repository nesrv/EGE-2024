
f = open("я-апрель-25-11/24 (1).txt")
s = f.read().split("AHAHA")

res = max(s, key=len)

print(res)
print(len(res))