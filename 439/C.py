n = int(input())
a = []

for y in range(n):
    for x in range(y):
        if(0 < x < y) and x**2 + y**2 <= n:
            a.append(x**2 + y**2) 

a = sorted(a)

if n != 0:
    print(len(a))
    print(" ".join(a))
else:
    print(n)
    print()