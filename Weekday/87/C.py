N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
heights = [0]*N
out = -1

for i in range(1,N):
    heights[i] = abs(A[i-1]-A[i])

prefix = [0]*N

for i in range(1,N):
    prefix[i] = prefix[i-1] + heights[i]


minK = (-1,10**10)
for ind,i in enumerate(prefix,start=1):
    if K <= i < minK[1]:
        minK = (ind,i)

for ind,i in enumerate(prefix,start=1):
    if i == minK[1]:
        out = ind
        break

print(out)
