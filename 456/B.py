import itertools
A = []
total = 0

for i in range(3):
    A.append(list(map(int,input().split())))

for i in list(itertools.product(*A)):
    print(i)
    if 4 in i and 5 in i and 6 in i:
        total += 1

print(total/216)