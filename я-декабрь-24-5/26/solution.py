# правильно 1731 55
# 1923 56
from math import ceil
f = open("я-декабрь-24-5/26/txt-2.txt")
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
    print(click, key, clicks[key])

print(*clicks.items(), sep="\n")


print(max_len-5)