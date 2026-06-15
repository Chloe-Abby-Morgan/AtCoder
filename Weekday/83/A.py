N,D = list(map(int,input().split()))
ab = [tuple(map(int,input().split())) for i in range(N)]
total = 0

for i in ab:
    total += i[0] + (i[1]*D)

print(total)