f = open('txt.txt')

S = [[int(t[0]), t[1]] for val in f if (t := val.split())]
S.sort(reverse=1)

SKL = []
while len(S) > 0:
    M = [S.pop(0)]
    i = 0
    while i < len(S):
        if M[-1][0] - S[i][0] >= 5 and M[-1][1] != S[i][1]:
            M.append(S.pop(i))
            i -= 1
        i += 1
    SKL.append(M)

print(len(SKL), len(SKL[0]))

f = open('26.txt')
box=[]
cklad =[]
for i in f:
    size, color = i.split()
    box.append([int(size),color])