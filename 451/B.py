N,M = list(map(int,input().split()))
A = []
B = []
term1 = 0
term2 = 0

for i in range(N):
    x = list(map(int,input().split()))
    A.append(x[0])
    B.append(x[1])

for i in range(1,M+1):
    term1, term2 = 0,0
    for j in A:
        if i == j:
            term1 += 1
    
    for j in B:
        if j == i:
            term2 += 1
    print(term2 - term1)