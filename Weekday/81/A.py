N = int(input())
ts = [input().split() for i in range(N)]
total = 0

for i in ts:
    if i[0] != i[1]:
        total += 1

print(total)