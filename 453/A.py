N = int(input())
S = input()
output = []

for i in range(N):
    if len(set(output)) == 1 and "o" in set(output) or (len(set(output)) == 0 and S[i] == "o"):
        continue
    output.append(S[i])

print("".join(output))
