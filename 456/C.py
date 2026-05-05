S = input()
width = 1
total = 0

while width != len(S)+1:
    left = 0

    print(S[:width])
    print(S[width-1:width])
    width += 1
print(total % 998244353)
