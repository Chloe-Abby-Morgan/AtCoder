T,X,Y = list(map(int,input().split()))
A = input()
B = input()

total = 0

for i in range(T):
    if A[i] == "R":
        X += 1
    elif A[i] == "L":
        X -= 1
    
    if B[i] == "R":
        Y += 1
    elif B[i] == "L":
        Y -= 1

    if X == Y:
        total += 1

print(total)