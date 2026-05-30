import math

N,M = list(map(int,input().split()))
H = list(map(int,input().split()))
TD = [list(map(int,input().split())) for i in range(M)]
H.insert(0,0)
H.append(0)
total = 0

for i in TD:
    H[i[0]] -= i[1]

    if i[0] >= 2: 
        H[i[0]-1] -= math.floor(i[1]/2)
    if i[0] <= N-1:
        H[i[0]+1] -= math.floor(i[1]/2)

for i in H[1:-1]:
    if i >= 1:
        total += 1

print(total)