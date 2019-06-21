class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, head):
        self.head = head

    def traverse_tree(self):
        queue = [self.head]
        ans = []
        while queue:
            head = queue.pop(0)
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)
            ans.append(head.value)
        return ans

    def deep_first_search(self):
        head = self.head
        stack = [head]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    def reverse_tree(self, head):
        temp = head.right
        head.right = head.left
        head.left = temp
        if head.left is not None:
            self.reverse_tree(head.left)
        if head.right is not None:
            self.reverse_tree(head.right)


node7 = TreeNode(8)
node6 = TreeNode(7)
node5 = TreeNode(6)
node4 = TreeNode(5)
node3 = TreeNode(4, left=node6, right=node7)
node2 = TreeNode(3, left=node4, right=node5)
node1 = TreeNode(2, left=node2, right=node3)

""" Resulting Binary Tree 

      2
    /   \
   3     4
  / \   /  \
 5   6 7    8

 traverse tree -> [2, 3, 4, 5, 6, 7, 8]
 deep_first_search -> [2, 3, 5, 6, 4, 7, 8]
"""

x = Tree(node1)
print(x.traverse_tree())
print(x.deep_first_search())

""" Reversed Binary Tree 

      2
    /   \
   4     3
  / \   /  \
 8   7 6    5

 traverse tree -> [2, 4, 8, 7, 3, 6, 5]
 deep_first_search -> [2, 4, 8, 7, 3, 6, 5]
"""

x.reverse_tree(node1)
print('reversed binary search tree:', x.traverse_tree())
print('bfs of reversed binary search tree:', x.deep_first_search())

