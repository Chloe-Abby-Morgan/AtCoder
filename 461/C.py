N,K,M = list(map(int,input().split()))
cv = sorted([tuple(map(int,input().split())) for i in range(N)],reverse=True,key=lambda x:x[1])
mV = [] # Most valuable for each colour
mmV = {}
taken = []
coloursTaken = 0
nCV = []

#Get most valuable per colour append to mV
for i in cv:
    if i[0] not in mmV:
        mV.append(i)
        mmV[i[0]] = True
    else:
        nCV.append(i)

mV = sorted(mV,key=lambda x : x[1])

#Get unique colours
while mV and coloursTaken < M:
    coloursTaken += 1
    taken.append(mV[-1][1])
    mV.pop()

nCV = sorted(nCV,key=lambda x:x[1])

#Get the rest
while len(taken) < K:

    if nCV and mV:
        if nCV[-1][1] > mV[-1][1]:
            taken.append(nCV[-1][1])
            nCV.pop()
        else:
            taken.append(mV[-1][1])
            mV.pop()
    elif nCV:
        taken.append(nCV[-1][1])
        nCV.pop()
    elif mV:
        taken.append(mV[-1][1])
        mV.pop()

print(sum(taken))