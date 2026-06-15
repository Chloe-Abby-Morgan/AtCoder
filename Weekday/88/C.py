N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
lr = sorted([list(map(int,input().split())) for i in range(M)])
LR = [lr[0]]
out = 0

for i in range(1,M):
    last = LR[-1]
    curr = lr[i]

    if curr[0] <= last[1]:
        last[1] = max(last[1],curr[1])
    else:
        LR.append(curr)

for left,right in LR:
    out += sum(A[left-1:right])

print(out)