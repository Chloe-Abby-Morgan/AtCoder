N = int(input())
xy = sorted([tuple(map(int,input().split())) for i in range(N)],reverse=True)
yx = sorted(xy,key=lambda x:x[1],reverse=True)
count = 0

maxY = xy[-1][1]
maxX = yx[-1][0]

for i in xy:
    if 0 <= i[0] <= maxX and 0 <= i[1] <= maxY:
        count += 1
        
print(count)