class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)
n6 = Node(3)
n7 = Node(3)


n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

#
# def check_if_mirror(root1, root2):
#     if root1 is None and root2 is None:
#         return True
#     if root1 is not None and root2 is not None:
#         if root1.val == root2.val:
#             return (check_if_mirror(root1.left, root2.right) and check_if_mirror(root1.right, root2.left))
#     return False
#
#
# def check_it(root):
#     return check_if_mirror(root, root)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right


class Tree_:
    def __init__(self, head):
        self.head = head

    def is_simmetric(self):

        def check_ends(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is not None and n2 is not None:
                if n1.val == n2.val:
                    return check_ends(n1.left, n2.right) and check_ends(n1.right, n2.left)
            return False

        return check_ends(self.head, self.head)


node1 = Node(1)
node2 = Node(2)
node3 = Node(2)
node1.left, node1.right = node2, node3
f = Tree_(node1)

print(f.is_simmetric())





