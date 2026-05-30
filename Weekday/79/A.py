N,M = list(map(int,input().split()))
S = [input() for i in range(N)]
flag = False

for i in range(N):
    if flag:
        break
    for j in range(M):
        if S[i][j] == "#":
            ad = []
            if i > 0:
                ad.append(S[i-1][j])
            if i < N-1:
                ad.append(S[i+1][j])
            if j > 0:
                ad.append(S[i][j-1])
            if j < M-1:
                ad.append(S[i][j+1])
            
            if 1 <= ad.count("#") <= 3:
                continue
            else:
                flag = True
                break

            
print("Yes" if not flag else "No")