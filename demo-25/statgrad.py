from collections import defaultdict, OrderedDict

f = '''
101	12	0
102	9	0
103	2	101;102
104	4	103
105	18	103
106	1	104
107	1	105;106
108	3	107
109	8	0
110	14	109
111	6	109
112	15	110;111
113	11	111
'''.strip().splitlines()

processes = {}

for proc in f:
    proc = proc.replace(';', '\t')
    proc = list(map(int, proc.split('\t')))
    if proc[2] == 0:
        processes[proc[0]] = [0, proc[1]]
    elif len(proc) == 4:
        max_proc = max(processes[proc[2]][-1], processes[proc[2]][-2])
        print(1, proc, max_proc)
        processes[proc[0]] = [max_proc , max_proc  + proc[1]]
    else:
        processes[proc[0]] = [processes[proc[2]][-1], processes[proc[2]][-1] + proc[1]]


print(*processes.items(), sep='\n')

times = {x:[] for x in range(38)}

for t in times:
    for proc, time in processes.items():
        if t in  range(time[0], time[-1]):
            times[t] += [proc]

print(*times.items(), sep='\n')

