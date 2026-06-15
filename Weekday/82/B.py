from collections import deque
N,K,M,X = list(map(int,input().split()))
Y = list(map(int,input().split()))
bai = deque(bin(X)[::-1][:-2])

while len(bai) != N:
    bai.append(0)

op = 0
while bai[0] != 1:
    if op < K:
        op += 1
        bai.popleft()
        bai.append(1)
    else:
        break
print(bai)

