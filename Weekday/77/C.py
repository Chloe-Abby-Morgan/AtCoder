N,S = list(map(int,input().split()))
A = list(map(int,input().split()))
A.sort(reverse=True)
taken = 0
total = 0
flag = False

for i in A:
    if total == S:
        flag = True
        break
    elif i + total <= S:
        total += i
        taken += 1

if flag:
    print(taken)
else:
    print(-1)
