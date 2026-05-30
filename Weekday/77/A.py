N,L,R,M = list(map(int,input().split()))
pk = []
total = 0
for i in range(N):
    pk.append(list(map(int,input().split())))

for i in pk:
    if L <= i[0] <= R and i[1] <= M:
        total += 1
        
print(total)