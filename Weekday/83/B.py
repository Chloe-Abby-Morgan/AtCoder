N,Q = list(map(int,input().split()))
H = list(map(int,input().split()))
Q = [tuple(map(int,input().split())) for i in range(Q)]
O = [0] * N

for i in range(N):
    if i != 0:
        l = H[max(H[0:i])]/(H[i]-(max(H[0:i])))
    else:
        l = 0

    if i != N-1:
        r = H[max(H[i:N-1])]/(max(H[i:N-1])-H[i])
    else:
        r = 0

    O[i] = 1/(1+l+r)

print(O)