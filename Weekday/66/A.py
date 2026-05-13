N,Q = list(map(int,input().split()))
A = list(map(int,input().split()))
A.append(0)
B = [int(input())-1 for i in range(Q)]

for i in B:
    A[i+1] += A[i]
    A[i] = 0

print(" ".join(list(map(str,A[:-1]))))