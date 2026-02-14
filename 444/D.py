N = input()

def ones(num):
    return int("1"*int(num))
    
A = (map(ones, input().split()))
print(sum(A))


