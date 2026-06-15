S = input()
ls = []
for i in S:
    if i.isdigit():
        ls.append(i)

print("".join(ls))
