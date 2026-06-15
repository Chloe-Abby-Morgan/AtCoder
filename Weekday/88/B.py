N,K = list(map(int,input().split()))
T = sorted(map(int,input().split()))

l,r = 0,0
total = 0

for i in range(N):
    if abs(T[l]-T[r]) > K:
        total += 1
        l = r
        r += 1
    else:
        r += 1

print(total+1 if len(T)>0 else 0)