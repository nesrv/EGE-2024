# правильно 1731 55
from collections import defaultdict

f = open("26/Я-2025-Д-clicker/txt.txt")
n = int(f.readline())
clicks = defaultdict(list)
first_click = int(f.readline())
clicks[first_click].append(first_click)

for click in f:
    click = int(click)
    if click <= first_click + 1000:
        clicks[first_click].append(click)
    else:             
        clicks[click].append(click)
        first_click = click

# print(*clicks.items(), sep="\n")
count_clicks = 0
max_count_click = 0

for key, value in clicks.items():
    # if len(value) > 5:
    max_count_click = max(max_count_click, len(value))
    # clicks[key] = value[:5]        
    count_clicks += len(clicks[key][:5])
    

print(count_clicks)
print(max_count_click-5)

