N = int(input())
P = list(map(int,input().split()))
out = 1
arr = [False]*(N+1)
arr[1] = True
nxt = P[0]

for i in range(N):
    if arr[nxt] == False:
        out += 1
        arr[nxt] = True
        nxt = P[nxt-1]
    else:
        break
print(out)