N = int(input())
X = sorted(map(int,input().split()),reverse=True)
total = 0
graph = {i : 0 for i in X}

for i in range(N):
    if graph[X[i]] == 0:
        graph[X[i]] += 1
        total += abs(X[i]-X[i-1])
    elif graph[X[i]] == 1:
        graph[X[i]] += 1
        total += abs(X[i]-X[i-2])
print(total)
