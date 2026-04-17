N = int(input())
A = [""]*N
B = [""]*N
S = []
WIndex = 0
Frequency = {}

for i in range(N):
    A[i], B[i] = list(map(int, input().split()))

M = int(input())

for i in range(M):
    S.append(input())
    for char in S[i]:
        if char in Frequency:
            Frequency[char] += 1
        else:
            Frequency[char] = 1

for word in S:
    workingF = Frequency.copy()
    index = 0
    for char in word:
        index += 1
        workingF[char] -= 1
        if workingF[char] < 0 or len(word) != B[index] or word[A[index]] != char:
            if index == len(word):
                print("No")
            else:
                continue
        elif index == len(word):
            print("Yes")
    WIndex += 1




