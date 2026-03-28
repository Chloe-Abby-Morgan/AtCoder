Q = int(input())
trees = {}

for i in range(Q):
    x = list(map(int, input().split()))

    if(x[0] == 1):
        if x[1] in trees:
            trees[x[1]] += 1
        else:
            trees[x[1]] = 1
        print(len(list(o for o in trees.values() if o > 0)))

    elif(x[0] == 2):
        for k,v in trees.items():
            if k <= x[1]:
                trees[k] = 0
        print(len(list(o for o in trees.values() if o > 0)))