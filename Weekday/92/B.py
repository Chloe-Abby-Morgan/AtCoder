N,L,T = list(map(int,input().split()))
xv = [tuple(map(int,input().split())) for i in range(N)]

for pos,vol in xv:
    traveledPos = (pos+(vol*T))
    
    # print(traveledPos)
    # if 0 <= traveledPos <= L:
    #     pass
    # elif traveledPos > L:
    #     pass
    # else:
    #     pass

    while (0 <= abs(traveledPos) <= L) == False:
        if traveledPos > L:
            traveledPos = abs(traveledPos) - L
        else:
            traveledPos = abs(traveledPos) + L

    print(abs(traveledPos))