N,M = list(map(int, input().split()))
F = list(map(int,input().split()))
types = [False]*M

if len(set(F)) == len(F):
    print("Yes")
else:
    print("No")

for i in range(1,M+1):
    if i in set(F):
        types[i-1] = True

if False in types:
    print("No")
else:
    print("Yes")
