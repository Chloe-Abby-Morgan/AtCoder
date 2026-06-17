from collections import deque
N,M,K = list(map(int,input().split()))
S = list(map(int,input().split()))
uv = [list(map(int,input().split())) for i in range(M)]
graph = {}
total = K
visited = set()

for U,V in uv:
    if U in graph:
        graph[U].append(V)
        if V in graph:
            graph[V].append(U)
        else:
            graph[V] = [U]
    else:
        graph[U] = [V]
        if V in graph:
            graph[V].append(U)
        else:
            graph[V] = [U]

def BFS(start):
    global visited
    global total

    q = deque()
    q.append(start)
    visited.add(start)

    while q:
        first = q.popleft()
        visited.add(first)
        if first in graph:
            for child in graph[first]:
                if child not in visited:
                    q.append(child)
                    total += 1


for i in S:
    BFS(i)

print(total)