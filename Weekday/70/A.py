N,Y,M = list(map(int,input().split()))
A,B,P,Q,C = [],[],[],[],[]
curr,nex = 0,0
for i in range(N):
    x = input().split()
    A.append(int(x[0]))
    B.append(int(x[1]))
    P.append(int(x[2]))
    Q.append(int(x[3]))
    C.append(int(x[4]))

for i in range(N):
    if P[i] == Y and Q[i] == M:
        curr += C[i]
    
    if P[i] == Y and Q[i] == M+1:
        nex += C[i]
    
    if M+1 > 12:
        if P[i] == Y+1 and Q[i] == 1:
            nex += C[i]
print(curr,nex)