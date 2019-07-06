# Binary Search Tree in array representation


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def sorted_array_to_bst(arr) -> object:
    """ Converts sorted array to a balanced BST.
    input : sorted array of integers
    output: root node of balanced BST
    :param arr:
    :return obj:
    """
    if not arr:
        return None
    mid = (len(arr)) // 2
    node = Node(arr[mid])
    node.left = sorted_array_to_bst(arr[:mid])
    node.right = sorted_array_to_bst(arr[mid + 1:])
    return node


def pre_order(node) -> int:
    """ A utility function to print the preorder traversal of the BST.
    :param node:
    :return int:
    """
    if not node:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


# Constructed balanced BST is
#      4
#    /   \
#   2    6
#  / \   / \
# 1  3  5  7


list_of_nodes_values = [1, 2, 3, 4, 5, 6, 7]
test_root = sorted_array_to_bst(list_of_nodes_values)
print("PreOrder Traversal of constructed BST ")
pre_order(test_root)
