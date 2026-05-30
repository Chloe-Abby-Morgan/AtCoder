N = int(input())
S = input()
comp = [S[0]]
cPoint = 0
total = 0
left = 0

for i in range(1,N):
    if S[i-1] == S[i]:
        continue
    else:
        comp.append(S[i])
comp = "".join(comp)

while S:
    for i in range(len(S)):
        if cPoint == len(comp)-1:
            total += 1
            break
        if S[i] == comp[cPoint]:
            cPoint += 1
    S = S[:-1]
    cPoint = 0

print(total,comp)