H,W = list(map(int,input().split()))
total = 0
S = []
for i in range(H):
   S.append(input().split())

for i in range(1, min(H,W) + 1):
   total += (H-i+1) * (W-i+1)
print(total)

