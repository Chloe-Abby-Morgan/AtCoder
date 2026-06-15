N,M = list(map(int,input().split()))
WL = [list(map(int,input().split())) for i in range(N)]
PC = [list(map(int,input().split())) for i in range(M)]
total = 0

for i in PC:
    WL[i[0]-1][0] += i[1]

for i in WL:
    if i[0] > i[1]:
        total += 1

print(total)