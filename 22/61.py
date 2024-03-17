from pprint import *

s = '''
1	97	0
2	149	0
3	44	1; 2
4	80	3
5	26	3
6	47	5
7	74	4; 6
8	82	0
9	137	0
10	90	8; 9
11	48	10
12	84	10
13	17	11
'''.strip().splitlines()


d = [(0, 0, 0, 0)]*(len(s)+1)

for elem in s:

    elem = list(map(int, elem.replace(';', '\t').split('\t')))
    num, dur, *subs = elem
    d[num] = [num, dur, dur, 0]
    max_dur = 0
    if subs[0] != 0:
        for x in subs:
            max_dur = max(max_dur, d[x][2])
    d[num][2] += max_dur
    if max_dur != 0:
        d[num][1] = max_dur
    else:
        d[num][1] = 0    
    d[num][3] = d[num][2] - d[num][1]
# pprint(d)
d[8] = [0, 0, 0]
d.sort(key = lambda x: (x[-3], x[-2]))
# dmax = max(d[1:], key= lambda x : x[-1])[-1]

pprint(d)
# print (dmax)
