import heapq

N,K = list(map(int,input().split()))
S = []

for i in range(N):
    x = input().split()
    S.append(int(x[0])+int(x[1]))

minH = S[:K]
heapq.heapify(minH)

for i in S[K:]:
    if i  > minH[0]:
        heapq.heapreplace(minH,i)
    
res = []

while minH:
    res.append(heapq.heappop(minH))

print(sum(res))

