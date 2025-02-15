# правильно 1731 55
# 1923 56
from math import ceil
f = open("26/Я-2025-Д-clicker/txt.txt")
n = int(f.readline())
clicks = {}
max_len = 0

for click in f:
    click = int(click)
    if click % 1000 == 0 and click !=0:
        clicks[click-1000] = [click] if click-1000 not in clicks else clicks[click-1000] + [click]
    else:
        key = click - click % 1000
        if key not in clicks:
            clicks[key] = [click]        
        else:
            clicks[key].append(click)
    max_len = max(max_len, len(clicks[key]))

max_len = max(len(x) for x in clicks.values() if len(x) > 0)
count_clicks = sum(len(x[:5]) for x in clicks.values() if len(x) > 0)
    
print(*clicks.items(), sep="\n")

print(max_len-5)
print(count_clicks)

# print(ceil(13,2))
# key = 1000
# clicks[key] = [first_click]

# max_len = 0

# for t in f:
#     if key - 1000 <= int(t) <= key:
#         clicks[key].append(int(t))
#     elif 
        
#     else:
#         slice_clicks = clicks[key][5:]
#         clicks[key] = clicks[key][:5]
#         max_len = max(max_len, len(slice_clicks))
#         key += 1000
#         clicks[key] = []
#         clicks[key].append(int(t))

# # количество элементов в списках clicks

# count_clicks = sum(len(x) for x in clicks.values() if len(x) > 0)

# print(*clicks.items(), sep="\n")

# print(max_len)
# print(count_clicks)
