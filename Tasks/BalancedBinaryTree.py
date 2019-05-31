from collections import defaultdict


d = defaultdict(list)
d['A'] = ['B', 'C']
print(d)


def addEdge(v, another_v):
    d[v].append(another_v)


addEdge('B', 'E')
addEdge('B', 'H')
addEdge('E', 'D')
addEdge('E', 'F')

print(d)


class Solution(object):
    def isBalanced(self, root):


        def balance(root):
            left = balance(root.left)
            right = balance(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return balance(root) != -1




