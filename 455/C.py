N,K = list(map(int,input().split()))
A = list(map(int, input().split()))
nums = set(A)
most = sum(A)
totalR = {}

for i in nums:
    total = 0
    for index,j in enumerate(A):
        if index == len(A)-1:
            if i == j:
                total += j
            totalR[i] = total
        if i == j:
            total += j
        else:
            continue

mostVal = list(totalR.values())
mostVal.sort(reverse=True)
for i in mostVal[:K]:
    most -= i

print(most if most >= 0 else 0)



