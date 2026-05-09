N = int(input())
L = []
for i in range(N):
    L.append(list(map(int,input().split()[1:])))
X,Y = list(map(int,input().split()))

print(L[X-1][Y-1])