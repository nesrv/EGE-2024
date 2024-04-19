f = open("26/задача 61 (банк)/26.txt")
N = int(f.readline())
a = sorted(list(map(int, x.split())) for x in f)
print(a[:10])
window_1 = []
window_2 = []

count = 0
usli = 0
for start, duration, window in a:
    
    if len(window_1) > 0 and window_1[0] <= start:
        window_1.pop(0)
    if len(window_2) > 0 and window_2[0] <= start:
        window_2.pop(0)
    
    if window == 1 or (window != 1 and window != 2 and len(window_1) <= len(window_2)):
        if window_1 == []:
            window_1.append(start + duration)
            count += 1
        elif len(window_1) < 12:
            window_1.append(window_1[-1] + duration)
            count +=1
        else:
            usli += 1
    else:
        if window_2 == []:
            window_2.append(start + duration)
        elif len(window_2) < 12:
            window_2.append(window_2[-1] + duration)
        else:
            usli += 1
print(count, usli)
