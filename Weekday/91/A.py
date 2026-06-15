N = int(input())
T = list(map(int,input().split()))
prefix = [0]*(N)

for i in range(1,N):
    prefix[i] = abs(T[i-1]-T[i])

print(min(prefix[1:]),max(prefix))