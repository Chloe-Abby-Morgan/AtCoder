N,M = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(N)]
B = []
C = []
for i in range(N):
    for j in range(1,M):
        B.append(abs(A[i][j] - A[i][j-1]))
    C.append(sum(B))
    B.clear()

print(C.index(max(C))+1)