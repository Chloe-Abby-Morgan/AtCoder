N = int(input())
tr = [tuple(map(int,input().split())) for i in range(N)]
longestR = max(tr,key=lambda x:x[1])
tr.remove(longestR)
time = 0

for T,R in tr:
    time += (T+R)

print(time+longestR[0])