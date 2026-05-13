N,M = list(map(int,input().split()))
A,B = [],[]
adj = [[] for i in range(M)]

for i in range(M):
    x = list(map(int,input().split()))
    adj[x[0]-1].append(x[1]-1)
    adj[x[1]-1].append(x[0]-1)


def DFS(vert,adj,visited,parent):
    visited[vert] = True

    for neighbor in adj[vert]:
        if not visited[neighbor]:
            if DFS(neighbor, adj, visited, vert):
                return True
        elif neighbor != parent:
            return True
    return False

def isCycle(adj):
    visited = [False] * M
    
    for i in range(M):
        if not visited[i]:
            if DFS(i, adj, visited, 0):
                return True
    return False

print("Yes" if isCycle(adj) else "No")