H,W = list(map(int, input().split()))
S = []
visited = set()
total = 0

for i in range(H):
    S.append(input())

def DFS(mat, x, y):
    if(x < 0 or x >= H or y < 0 or y >= W):
        return
    if mat[x][y] == "#" or (x,y) in visited:
        return
        
    visited.add((x,y))

    DFS(mat, x+1, y)
    DFS(mat, x-1, y)
    DFS(mat, x, y+1)
    DFS(mat, x, y-1)

for i in range(H):
    for j in range(W):
        if (S[i][j] == "." and (i,j) not in visited):
            total += 1
            DFS(S, i, j)

for i in range(W):
    if S[0][i] == "." or S[0][W-1] == ".":
        total -= 1

for i in range(H):
    if S[i][0] == "." or S[i][W-1] == ".":
        total -= 1

print(total)

