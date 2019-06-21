class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

    def get_next_node(self):
        return self.next

    def set_next_node(self, N):
        self.next = N
        return


class List(object):
    def __init__(self, node):
        self.head = node


def reverse_list(l):
    prev = None
    current = l.head
    nex = current.get_next_node()

    while current:
        current.set_next_node(prev)

        prev = current
        current = nex
        if nex:
            nex = nex.get_next_node()

    l.head = prev


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4
list_ = List(n1)

reverse_list(list_)
print(list_.head.val)
print(list_.head.next.val)
print(list_.head.next.next.val)






