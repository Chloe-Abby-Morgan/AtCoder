N,L,K,Y = list(map(int,input().split()))
A = list(map(int,input().split()))
B = []
C = []
total = 0

for i in A:
    if i > L:
        B.append(i)

for i in range(len(B)):
    B[i] -= Y

for i in B:
    if i > L:
        total += 1
    else:
        C.append(i)

k = 0
for i in range(len(C)):
    if k == K:
        break
    total += 1
    k += 1

print(total)