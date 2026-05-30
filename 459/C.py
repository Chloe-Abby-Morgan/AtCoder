N,Q = list(map(int,input().split()))
arr = [0]*N
queries = [list(map(int,input().split())) for i in range(Q)]
timesFilled = 0

for action,x in queries:

    #increment - O(1)
    if action==1:
        arr[x-1] += 1

    #minus 1 - O(1)
        if timesFilled not in set(arr):
            timesFilled += 1

    #print - O(n)
    elif action==2:
        print(len(list(i for i in arr if i - timesFilled >= x)))