N,Q = list(map(int,input().split()))
W = list(map(int,input().split()))
L = [tuple(map(int,input().split())) for i in range(Q)]
A = [0] * (N+1)
D = [0] * (N+1)
total = 0

for i in L:
    A[i[0]-1] += i[2]
    A[i[1]] -= i[2]

D[0] = A[0]

for i in range(1,N):
    D[i] = D[i-1] + A[i]

for i in range(len(W)):
    if W[i] - D[i] <= 0:
        total += 1

print(total)

