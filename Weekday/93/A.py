N,M = list(map(int,input().split()))
W = list(map(int,input().split()))
ka = [list(map(int,input().split()))[1:] for i in range(M)]

for i in ka:
    total = 0
    for j in i:
        total += W[j-1]
    print(total)