N,M = list(map(int,input().split()))
R = list(map(int,input().split()))
FS = [list(map(int,input().split())) for i in range(M)]
total = 0

for i in FS:
    if R[i[0]-1] >= i[1]:
        R[i[0]-1] -= i[1]
        total += 1

print(total)