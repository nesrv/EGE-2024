from statistics import mean
f = '''
8
4 4 4 4 4
7 5 5 5 2
10 3 4 4 5
1 4 4 4 3
6 3 5 5 3
2 2 2 2 2
13 2 2 2 3
3 3 3 3 3

'''.strip().splitlines()
# 52326 635
f = open('25/demo_2025_26.txt')
n = int(f.readline())

a = [list(map(int,s.split())) for s in f]
passed = filter(lambda x: x[1:].count(2)==0, a)
passed = sorted(passed, key = lambda x: (-mean(x[1:]),x[0]))
passed = passed[:int(len(a)*0.25)]
print(passed[-1])

failed = filter(lambda x: x[1:].count(2)>2, a)
failed = sorted(failed, key = lambda x: ((x[1:-1]).count(2), x[0]))
print(failed[0])

# for i in range(len(a)):
#     grades = a[i][1:]
#     avg_grades = mean(grades)
#     a[i].append(avg_grades)
  
# passed = [x for x in a if x[1:-1].count(2)==0] #сдали
# через filter

# passed = sorted(passed, key = lambda x: (-x[-1],x[0]))


# passed.sort(key = lambda x: (-x[-1],x[0]))
# 25 % процентов





