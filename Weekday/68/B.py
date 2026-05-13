N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
L,R = [],[]
B = [0]*M

for i in range(M):
    x = input().split()
    L.append(int(x[0]))
    R.append(int(x[1]))

for i in range(M):
    B[i] = sum(A[L[i]-1:R[i]])

print(max(B) - min(B))
