N = int(input())
S = input()
steps = [0]*N
steps[1] = 1
steps[2] = 1

for i in range(N):
    if S[i] == "#":
        continue

    if i >= 1:
        steps[i] += steps[i-1]
    if i >= 2:
        steps[i] += steps[i-1] + steps[i-2]
    if i >= 3:
        steps[i] += steps[i-1] + steps[i-2] + steps[i-3]
    
print(steps[-1] % (10**9+7))
