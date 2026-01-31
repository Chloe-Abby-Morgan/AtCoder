N,T = map(int, input().split())
A = list(map(int,input().split()))
A.insert(0, 0)

openTime = 0
trueArr = []
Ftime = 0
ef = False

if T != A[-1]:
    A.append(T)
    ef = True
if ef:
    for i in range(1,N+2):
        if A[i] - Ftime < 100:
            continue
        else:
            trueArr.append(A[i])
            Ftime = A[i]
else:
    for i in range(1,N+1):
        if A[i] - Ftime <= 100:
            continue
        else:
            trueArr.append(A[i])
            Ftime = A[i]

for i in range(len(trueArr)):
    if i == 0:
        openTime += trueArr[0]
    else:
        openTime += trueArr[i] - trueArr[i-1] - 100
print(openTime)


