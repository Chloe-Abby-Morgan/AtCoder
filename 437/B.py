H,W,N = map(int, input().split())
AHW = []
BN = []
for i in range(H):
    AHW.append(list(map(int, input().split())))
for i in range(N):
    BN.append(int(input()))
result = 0

for lst in AHW:
    last_result = 0
    for elt in lst:
        if elt in BN:
            last_result += 1
    if last_result > result:
        result = last_result
print(result)