N = input()
total = 0
def ones(num):
    return int("1"*int(num))
    
A = input().split()
for i in A:
    total += ones(i)

print(total)


