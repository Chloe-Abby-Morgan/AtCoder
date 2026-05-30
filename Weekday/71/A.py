S = input()
depth = 0
maxDepth = 0
for i in S:
    depth = max(depth,maxDepth)
    if i == "(":
        maxDepth += 1
    else:
        maxDepth -= 1
print(depth)