pinput = [8, 6, 10, 5, 7]
pSet = []
intPairs  = []
l = 1
r = 1

pinput.sort()

for i in range(len(pinput)):
    while r <= len(pinput):
        pSet.append((l,r))
        r += 1
    l += 1
    r = 1

for elt in pinput:
    for i in pSet:
        if 1 <= i[0] <= i[1] <= len(pinput) and i[0] != i[1]:
            if i not in intPairs:
                intPairs.append(i)

for elt in intPairs:
    ar = 0
    for i in range(elt[1]):
        ar += pinput[i]
        print(elt, pinput[i])
print(intPairs)