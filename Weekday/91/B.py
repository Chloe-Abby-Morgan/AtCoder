N,K = list(map(int,input().split()))
C = []
medians = [0]*N
total = 0

for i in range(N*2):
    if i % 2 == 1:
        C.append(sorted(map(int,input().split())))
    else:
        input()

for i in range(N):
    medians[i] = C[i][int((len(C[i])+1)/2)-1]
    
medians.sort(reverse=True)

for i in range(K):
    if medians[i] >= 0:
        total += medians[i]
    
print(total)
