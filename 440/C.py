T = int(input())
result = []


for case in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    total = 0
    
    for i in enumerate(C):
        for x in range(1, 2*W):
            if (C[i[0]]+x) % (2*W) > W:
                total += C[i[0]]
                break

    result.append(str(total))
print("\n".join(result))

