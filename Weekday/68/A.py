N,L,R = list(map(int,input().split()))
T = [int(input()) for i in range(N)]

total = 0

for i in T:
    if L <= i <= R:
        total += 1

print(total)