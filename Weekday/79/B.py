N,K = list(map(int,input().split()))
tp = list(map(int,input().split()))
C = sorted(list(map(int,input().split())),reverse=True)

discounts = [0]*100
print(tp)
    
print(discounts)

prefix = [0]*N
prefix[0] = C[0]

for i in range(1,N):
    prefix[i] = prefix[i-1] + C[i]

print(prefix)

