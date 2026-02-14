N = int(input())
S = []
Sl = []
Sdot = []

for i in range(N):
    S.append(input())

Sl = list(map(len, S))

for i in S:
   Sdot.append(max(Sl) - len(i))

for i in range(len(S)):
    print((Sdot[i]//2) * "." + S[i] + (Sdot[i]//2) * ".")

