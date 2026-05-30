N = int(input())
A = list(map(int,input().split()))
prefix = [0] * N
prefix[0] = A[0]
out = 0

for i in range(1,N):
    prefix[i] = prefix[i-1] + A[i]

for i in range(N):
    if (i+1)*A[i] >= prefix[i]:
        out += 1

print(out)