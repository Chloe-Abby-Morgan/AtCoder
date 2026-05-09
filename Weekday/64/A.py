N,K = list(map(int,input().split()))
A = sorted(list(map(int, input().split())))
total = 0
curr = set()

for i in A:
    if curr:
        if i >= K:
            curr.add(i)
        else:
            curr.clear()
            total += 1
    else:
        curr.add(i)
print(total if not curr else total + 1)