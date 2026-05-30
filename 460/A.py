N,M = list(map(int,input().split()))
operations = 0

while M != 0:
    M = N % M
    operations += 1

print(operations)