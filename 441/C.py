N,K,X = map(int, input().split())
A = sorted(list(map(int, input().split())))
A = A[:K]
cups = 0
total = 0

if sum(A) >= X:
    for i in A:
        if total < X:
            cups += 1
            total += i
        else:
            break
else:
    cups = -1
print(cups)
