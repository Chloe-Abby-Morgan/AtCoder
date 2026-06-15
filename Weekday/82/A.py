N,M,K = list(map(int,input().split()))
A = list(map(int,input().split()))
S,P,D = [],[],[]

for i in range(M):
    x = list(map(int,input().split()))
    S.append(x[0])
    P.append(x[1])
    D.append(x[2])

total = 0

for i in range(M):
    if S[i] == 1:
        total += max(A[P[i]-1]-K,0)*D[i]
    else:
        total += A[P[i]-1]*D[i]

print(total)