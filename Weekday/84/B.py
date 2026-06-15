    N,M = list(map(int,input().split()))
    T = list(map(int,input().split()))
    SC = sorted([tuple(map(int,input().split())) for i in range(M)])
    freq = {}
    mp = {i :False for i in set(T)}
    total = 0   

    for s,c in SC:
        if s in mp:
            mp[s] = True

    if False not in mp.values():

        for i in T:
            freq[i] = freq.get(i,0) + 1
        for s,c in SC:
            if s in freq:
                if freq[s] > 0:
                    total += freq[s] * c
                    freq[s] = 0

        print(total)
    else:
        print(-1)