f = open("27/ДЕМО-2025/txt.txt")

f.readline()
ans = []
min_summ = 10**10
stars = [list(map(float, s.replace(',','.').split())) for s in f]

for i in range (len(stars) - 1):
    for j in range(i+1, len (stars) - 1):
        center1 = stars[i]
        center2 = stars[j]
        summ = 0
        for star in stars:
            d1 = ((star[0] - center1[0]) ** 2 + (star[1] - center1[1]) ** 2)**0.5
            d2 = ((star[0] - center2[0]) ** 2 + (star[1] - center2[1]) ** 2)**0.5
            summ += min(d1, d2)
        if summ < min_summ:
            min_summ = summ
            ans = [center1, center2]

print((ans[0][0] + ans[1][0]) / 2 * 10000, (ans[0][1] + ans[1][1]) / 2 * 10000)