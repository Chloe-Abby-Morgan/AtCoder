N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

Aa = sorted(enumerate(A, start=1))
Bb = sorted(enumerate(B, start=1),key=lambda x:x[1])

flag = False

for i in range(N):
    if sorted(Aa[i]) == sorted(Bb[i]):
        continue
    else:
        flag = True

if flag:
    print("No")
else:
    print("Yes")