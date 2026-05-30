N = int(input())
A = list(map(int,input().split()))

prefix = [0]*N
prefix[0] = A[0]
rans = []

for i in range(1,N):
    prefix[i] = prefix[i-1] + A[i]

prefix.insert(0,0)

for l in range(N):
    r = N-1
    while 0 in A[l:r]:
        r -= 1
    rans.append(abs(A[l]-A[r]))
print(rans)
