S = list(input())
frequency = {}
void = []

for char in S:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

maxi = sorted(frequency.items(), key = lambda x : x[1], reverse=True)[0][1]
for pair in sorted(frequency.items(), key = lambda x : x[1], reverse=True):
    if maxi in pair:
        continue
    else:
        void.append(pair[0])

for char in S[:]:
    if char not in void:
        S.remove(char)

print("".join(S))