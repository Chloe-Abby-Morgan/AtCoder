S = list(input())
T = list(input())

def task(Ss, Tt, count):

    if Ss == Tt:
        return count
    else:
        for char in Ss:
            if char != "A" and char not in T:
                count = -1
                return count
            
        for index, char in enumerate(Ss):
            if char != "A":
                sStart = index
                break

        for index, char in enumerate(Tt):
            if char != "A":
                tStart = index
                break

        count += (sStart - tStart)
        if len(Ss) < len(Tt):
            count += (len(Tt) - len(Ss) - 1)
            for i in range((len(Tt) - len(Ss))):
                for ind, j in enumerate(Ss):
                    if j != "A":
                        Ss.insert(ind, "A")
                        break
    print(Ss, Tt)
    return task(Ss[sStart], Tt[tStart], count)

print(task(S, T, 0))