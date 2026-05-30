N,M,K = list(map(int,input().split()))
A = list(map(int,input().split()))
vals = []
l,r = 0,0

while l < N-K+1:
    print(A[l:r+1])
    if r-l+1 >= K or r >= N:
        l += 1
        r = l
    if r+1 < N and r-l+1 < K:
        r += 1
    vals.append(sum(A[l:r]))
print(sorted(vals,reverse=True))
print(sum(sorted(vals,reverse=True)[:M]))
    