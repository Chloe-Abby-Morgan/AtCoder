N, M = map(int, input().split())
S = list(input())
T = list(input())
Q = int(input())
W = []


for i in range(Q):
    W.append(list(input()))

for i in range(Q):
    index = 0

    for char in W[i]:
        index += 1
        if char in S and char in T:
            if index == len(W[i]):
                print("Unknown")
                break
            else:
                continue
        elif char in S and char not in T:
            print("Takahashi")
            break
        elif char in T and char not in S:
            print("Aoki")
            break
        