N,K = map(int, input().split())
total = 0
for i in range(N+1):
    if sum(list(map(int,list(str(i))))) == K:
        print(i)
        total += 1
print(total)
