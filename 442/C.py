N,M = map(int, input().split())
C = []
conflicts = {}
for i in range(M):
    C.append(list((map(int, input().split()))))

#Jank but works
for conflict in C:
    try: 
        if conflict[1] not in conflicts[conflict[0]]:
            aLst = conflicts[conflict[0]]
            aLst.add(conflict[1])
            aLst.add(conflict[0])
            conflicts.update({conflict[0] : aLst})
    except:
        conflicts.update({conflict[0] : {conflict[0]}})
        aLst = conflicts[conflict[0]]
        aLst.add(conflict[1])
        conflicts.update({conflict[0] : aLst})

for i in range(1, N+1):
    if i not in conflicts:
        conflicts.update({i : {i}})
print(conflicts)