N,M = list(map(int,input().split()))
uvc = [list(map(int,input().split())) for i in range(M)]
teams = [[i+1] for i in range(N)]
total = 0
dic = {i:i for i in range(N)}

for i in uvc:
    teams[dic[i[0]-1]].extend(teams[dic[i[1]-1]])
    teams[dic[i[1]-1]].clear()
    dic[i[1]-1] = dic[i[0]-1]

for i in teams:
    if i:
        total += 1

print(total)




