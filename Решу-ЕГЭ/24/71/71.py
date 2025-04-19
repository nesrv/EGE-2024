s = open('24/71/71.txt').readline()
abc = 'UVWXYZ'
d = {key:[] for key in abc}
max_l = 0
l = 0
for i in range(len(s)):
    if s[i] in abc:
        d[s[i]].append(i)
        if len (d[s[i]]) > 100:
            l = max(l, d[s[i]][0])
            del d[s[i]][0]
    max_l = max(max_l, i - l)

print(max_l)

