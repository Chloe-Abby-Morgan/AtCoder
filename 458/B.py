H,W = list(map(int,input().split()))
grid = []

for i in range(H):
    grid.append([0] * (W+2))

#top
grid.insert(0,[-1]*(W+2))
#bottom
grid.append([-1]*(W+2))

for i in range(H+1):
    for j in range(W):
        if j == 0:
            grid[i][j] = -1
for i in range(H+1):
    grid[i][-1] = -1

for i in range(1,H+1):
    for j in range(1,W+1):
        #down
        if grid[i-1][j] != -1:
           grid[i][j] += 1
        #up
        if grid[i+1][j] != -1:
           grid[i][j] += 1
        #left
        if grid[i][j-1] != -1:
           grid[i][j] += 1
        #right
        if grid[i][j+1] != -1:
           grid[i][j] += 1
        

        
for i in range(1,H+1):
    print(" ".join(map(str,grid[i][1:-1])))
