f = open('26/31 (unix время)/26.txt')

n = int(f.readline())
L = []

w0 = 1_634_515_200

w1 = w0 + 7 * 24 * 3_600
i=0
for times in f:
    start, end = map(int, times.split())
    if end == 0:
        end = w1
    if start >= w1 or end <= w0:
        continue
    L += (max(start, w0), 1), (min(end, w1), -1)
   
L.sort()

mxk = k = 0

for t, dk in L:
    k += dk
    if k > mxk:
        mxk, dt = k, 0
    if k - dk == mxk:
        dt += t - t0
    t0 = t
print(mxk, dt)
