N = int(input())
K = [list(map(int,input().split())) for i in range(N)]
gifts = {i:[] for i in range(1,N+1)}

for i in range(N):
   for j in K[i][1:]:
      gifts[j].append(i+1)

for i in range(1,N+1):
   if len(gifts[i]) > 0:
        print(len(gifts[i]), " ".join(map(str,gifts[i])))
   else:
        print(0)