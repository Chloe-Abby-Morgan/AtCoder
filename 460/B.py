import math
T = int(input())
X,Y,R,x,y,r = [],[],[],[],[],[]

for i in range(T):
    q = list(map(int,input().split()))
    X.append(q[0])
    Y.append(q[1])
    R.append(q[2])
    x.append(q[3])
    y.append(q[4])
    r.append(q[5])

for i in range(T):
    d = math.sqrt(abs(X[i]-x[i])**2 + abs(Y[i]-y[i])**2)
    if abs(R[i]-r[i]) <= d < r[i]+R[i]:
        print("Yes")
    else:
        print("No")