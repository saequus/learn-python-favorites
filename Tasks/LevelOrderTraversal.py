class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderTraversal(root):

    if not root:
        return []

    queue = [(root, 0)]
    res = []
    while queue:
        node, depth = queue.pop()

        if depth > len(res) - 1:
            res.append([node.val])
        else:
            res[depth] += [node.val]

        if node.left:
            queue += [(node, depth + 1)]

        if node.right:
            queue += [(node, depth + 1)]

    return res


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(levelOrderTraversal(root))
