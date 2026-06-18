import math
N,A,B,C = list(map(int,input().split()))
print((math.factorial(A)+math.factorial(B)+math.factorial(C))/N%(10**9+7))