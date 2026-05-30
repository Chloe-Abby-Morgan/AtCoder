N,M = list(map(int,input().split()))
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
total = 0
a = 0
b = 0

while a < N and b < M:
    if B[b] <= A[a]*2:
        total += 1
        a += 1
        b += 1
    elif B[b] > A[a]*2:
        a += 1
    else:
        b += 1

print(total)
