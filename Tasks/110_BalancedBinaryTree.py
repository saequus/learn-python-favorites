def is_tree_balanced(tree):
    root = tree.root

    def balance(root):
        left = balance(root.left)
        right = balance(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return balance(root) != -1


