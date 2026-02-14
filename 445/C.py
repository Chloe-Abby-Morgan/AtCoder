N = int(input())
A = list(map(int, input().split()))
toCell = {}
rList = []

for cell in range(1,len(A)+1):
    toCell[cell] = A[cell-1]

def findEnd(ind, see):
    if ind in see:
        return ind
    else:
        see.add(ind)
        return findEnd(toCell[ind], see)

for i in A:
    rList.append(str(findEnd(i, set())))
print(" ".join(rList))
