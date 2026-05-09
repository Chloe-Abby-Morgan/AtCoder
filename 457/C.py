import itertools
N,K = list(map(int,input().split()))
L = []
ListLen = []
B = [0] * N
prefix = []
upper = 0
lower = 0

for i in range(N):
    x = list(map(int,input().split()))
    ListLen.append(x[0])
    L.append(x[1:])

C = list(map(int,input().split()))

for i in range(len(ListLen)):
    B[i] = ListLen[i] * C[i]
prefix = list(enumerate(itertools.accumulate(B)))


#possible binary search
for ind, i in prefix:
    if i > K:
        lower = ind-1
        upper = ind
        break

print(L[upper-lower-K][0])

