

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        int_min = -2345857205
        int_max = 2345857205
        return self.BSTvalidation(root, int_min, int_max)

    def BSTvalidation(self, root, mini, maxi):

        if root is None:
            return True

        if root.val < mini or root.val > maxi:
            return False

        return self.BSTvalidation(root.left, mini, root.val - 1) and self.BSTvalidation(root.right, root.val + 1, maxi)


f1 = TreeNode(1)
f2 = TreeNode(2)
f3 = TreeNode(3)
f4 = TreeNode(2)
f5 = TreeNode(8)
f2.left = f1
f2.right = f3
f3.right = f5
f3.left = f4

ref = Solution()
print(ref.isValidBST(f2))




# another test

class AnotherTreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class isBSTValid():
    def isValid(self, node):
        mini = -238592003
        maxi = 238592003
        return self.checkValid(node, mini, maxi)

    def checkValid(self, node, mini, maxi):

        if node is None:
            return True

        if node.val < mini or node.val > maxi:
            return False

        return self.checkValid(node.left, mini, node.val - 1) and self.checkValid(node.right, node.val + 1, maxi)


node1 = AnotherTreeNode(5)
node2 = AnotherTreeNode(7)
node3 = AnotherTreeNode(3)
node4 = AnotherTreeNode(6)
node5 = AnotherTreeNode(8)
node1.left = node3
node1.right = node2
node2.left = node4
node2.right = node5

chh = isBSTValid()
print(chh.isValid(node1))


