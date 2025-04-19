from pprint import *

s = open("22/txt1.txt").read().split("\n")


d = [0]*13

for elem in s:
    elem = list(map(int, elem.replace(';', ' ').split()))
    num, dur, *subs = elem
    d[num] = [num, dur, dur]
    max_dur = 0
    if subs[0] !=0:      
      for x in subs:          
          max_dur = max(max_dur, d[x][2])
    d[num][2] += max_dur


dmax = max(d[1:], key= lambda x : x[-1])[-1]
# pprint(d) 

print(dmax)
