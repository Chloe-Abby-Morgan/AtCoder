N = int(input())
L = list(map(int, input().split()))
tree = []
treeDict = {}
L.append(None)
total = 0

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value, self.left, self.right}"
    
root = Node(0.5)
root.left = root.value - L[0]
root.right = root.value + L[0]

queue = [root]
tree = []
level = 0

while queue:
    tree.append([])
    for i in range(len(queue)):
        node = queue.pop(0)
        tree[level].append(node.value)

        if L[level+1] is not None:
            lnode = Node(node.value - L[level])
            lnode.left = lnode.value - L[level+1]
            lnode.right = lnode.value + L[level+1]
            queue.append(lnode)

            rnode = Node(node.value + L[level])
            rnode.left = rnode.value - L[level+1]
            rnode.right = rnode.value + L[level+1]
            queue.append(rnode)

    level += 1

# for level in tree:
#     for val in level:
#         print(val, end=" ")
#     print()

#DFS
# visited = set()
# stack = [tree[0][0]]

# while stack:
#     node = stack.pop()
#     if node not in visited:
#         visited.add(node)
#         print(node)
#         stack.extend()

print(tree)