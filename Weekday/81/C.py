N,M,S = list(map(int,input().split()))
graph = {}
U,V = [],[]
visited = set()
q = [S]
d = 0

for i in range(M):
    x = list(map(int,input().split()))
    if x[0] in graph:
        graph[x[0]].append(x[1])
    else:
        graph[x[0]] = [x[1]]

visited.add(S)

while q:
    first = q.pop(0)
    if len(visited) == N:
        break
    if first in graph:
        d += 1
        for neighbour in graph[first]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)


if len(visited) != N:
    print(-1)
else:
    print(d)

