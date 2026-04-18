N,M = list(map(int, input().split()))
A,B = [],[]
types = 0
graph = {}

for i in range(M):
    x = list(map(int,input().split()))
    A.append(x[0])
    B.append(x[1])

for i in range(M):
    if A[i] not in graph:
       graph[A[i]] = {B[i]}
    else:
        graph[A[i]].add(B[i])

def DFS(graph, start):
    global types
    visited, stack = set([start]), [start]
    while stack:
        last = stack.pop()
        types += 1
        if last in graph:
            for i in graph[last]:
                if i not in visited:
                    visited.add(i)
                    stack.append(i)
DFS(graph, 1)
print(types)