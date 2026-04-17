T,X = list(map(int, input().split()))
A = list(map(int, input().split()))
lastReading = A[0]

print("0", lastReading)

for time, temp in enumerate(A[1:]):
    if abs(lastReading - temp) >= X:
        print(time+1, temp)
        lastReading = temp