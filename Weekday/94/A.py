N,W = list(map(int,input().split()))
V = list(map(int,input().split()))
total = W

for i in V:
    if i <= total:
        total += i

print(total)