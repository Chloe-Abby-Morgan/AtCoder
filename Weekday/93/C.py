import itertools
N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
lrd = [tuple(map(int,input().split())) for i in range(M)]
pr = [0]*(N+1)

for L,R,D in lrd:
    pr[L-1] += D
    pr[R] -= D

pr = list(itertools.accumulate(pr))
new = [0]*N

for i in range(N):
    new[i] = A[i] + pr[i]

print(" ".join(map(str,new)))