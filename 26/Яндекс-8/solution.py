f = open('26.txt').readlines()
workers, requests = map(int, f.pop(0).split())

f = [int(x) for x in f]
f.sort()
print(workers, requests, f)
time = 60

storage = []
while f:
    l = [f.pop(0)]
    i = 0
    while i < len(f):
        if f[i] >= l[-1] + 60:
            l.append(f.pop(i))
            continue
        i += 1

    storage.append(l)
storage = storage[:workers]
storage.sort(key = lambda x: len(x), reverse=True)
print(sum([len(x) for x in storage]), len(storage[-1]))