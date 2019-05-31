class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

    def getNxtNode(self):
        return self.next

    def setNxtNode(self, N):
        self.next = N
        return


class List(object):
    def __init__(self, node):
        self.head = node


def reverseList(l):
    prev = None
    current = l.head
    nex = current.getNxtNode()

    while current:
        current.setNxtNode(prev)

        prev = current
        current = nex
        if nex:
            nex = nex.getNxtNode()

    l.head = prev


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4
list_ = List(n1)

reverseList(list_)
print(list_.head.val)
print(list_.head.next.val)
print(list_.head.next.next.val)






