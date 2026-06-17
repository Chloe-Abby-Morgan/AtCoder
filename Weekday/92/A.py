N,Q = list(map(int,input().split()))
S = list(map(int,input().split()))
C = list(map(int,input().split()))
Q = [list(map(int,input().split())) for i in range(Q)]
open = [True] * N

for i in Q:
    if i[0] == 1:
        for j in range(i[1]-1,i[2]):
            if open[j]:
                C[j] += i[3]
    elif i[0] == 2:
        open[i[1]-1] = False
    elif i[0] == 3:
        total = 0
        for j in range(i[1]-1,i[2]):
            if open[j] and C[j] <= 0:
                total += S[j]
        print(total)