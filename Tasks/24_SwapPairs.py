# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def traverse(self):
#         node = self
#         while node:
#             print(node.val)
#             node = node.next
#
# class SpecialList:
#     def __init__(self):
#         self.head = Node
#
#     def listprint(self):
#         printval = self.head
#         while printval is not None:
#             print(printval.val)
#             printval = printval.next
#
#     def atBegining(self, data_in):
#         newNode = Node(data_in)
#         newNode.next = self.head
#         self.head = newNode



# l1 = SpecialList()
# l1.head = Node(12)
# node1 = Node(29)
# node2 = Node(34)
# node3 = Node(34)
# node4 = Node(51)
#
# l1.head.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# l1.atBegining(100)
# print(l1.listprint())



# print(node1.next.val)
# print(node1.traverse())
#
#
#
# class Days:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def traverse(self):
#         node = self
#         while node:
#             print(node.val)
#             node = node.next
#
#     def addday(self, newdata, b=None):
#         newDay = Days(newdata)
#
#
#
# day1 = Days('Monday')
# day2 = Days('Tuesday')
# day3 = Days('Wednesday')
#
# day1.next = day2
# day2.next = day3
#
# print(day1.traverse())


#
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def traverse(self):
#         node = self
#         while node:
#             print(node.val)
#             node = node.next
#
#
# class SpecialList:
#
#     def __init__(self):
#         self.head = Node
#
#     def printlist(self):
#         node = self.head
#         while node:
#             print(node.val)
#             node = node.next
#
#     def addBefore(self, value):
#         head = self.head
#         newNode = Node(value)
#         newNode.next = head
#         self.head = newNode


# - - - - - - - - - - - - - - - -

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node:
            print(node.val)
            node = node.next


class SpecialList(object):
    def __init__(self):
        self.head = Node

    def printlist(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def addBefore(self, value):
        head = self.head
        newNode = Node(value)
        newNode.next = head
        self.head = newNode

    def addAfter(self, val):
        node = self.head
        newNode = Node(val)
        while node:
            print(node.val)
            if not node.next:
                node.next = newNode
                break
            node = node.next

    def addMiddle(self, position, val):
        node = self.head
        newNode = Node(val)
        while node:
            if node.val == position:
                nextNode = node.next
                node.next = newNode
                newNode.next = nextNode
                break
            node = node.next

    # def swapPairs(self, head):
    #     prev = Node(0)
    #     prev.next = head
    #     node = prev
    #     while node.next and node.next.next:
    #         next_node = node.next
    #         temp_value = node.val
    #         temp_next = node.next
    #         node.val = next_node.val
    #         next_node.val = temp_value
    #         print(next_node.val, 'next_node value')
    #         node.next = next_node.next
    #         next_node.next = temp_next
    #         print(next_node.next, 'next_node next')
    #         node = node.next

    def swapPairs(self):
        prev = Node(0)
        prev.next = self.head
        node = prev

        while node.next and node.next.next:
            first = node.next
            second = node.next.next

            # change the pointers to the swapped pointers
            node.next = second
            first.next = second.next
            second.next = first
            node = node.next.next

        self.head = prev.next

    def swap(self):
        head = self.head
        if head is None:
            return head
        elif head.next is None:
            return head
        else:
            res = head
            total = 0
            before = head
            while head is not None:
                if head.next is not None:
                    temp = head
                    temp1 = head.next
                    temp.next = head.next.next
                    temp1.next = temp
                    head = head.next
                    if total == 0:
                        total += 1
                        res = temp1
                    else:

                        before.next = temp1

                    before = temp
                else:
                    break
            return res



node1 = Node(29)
node2 = Node(31)
node3 = Node(34)
node4 = Node(39)

node1.next = node2
node2.next = node3
node3.next = node4

l1 = SpecialList()
l1.head = node1
print(l1.printlist())
l1.swap()
print(l1.printlist())

# - - - - - - - - - - - - - - - -

#
# # Definition for singly-linked list.
#
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def __init__(self):
#         self.main = ListNode
#
#     # def swapPairs(self, head):
#     #     node = self.main
#     #     while node:
#     #         next_node = node.next
#     #         temp_value = node.val
#     #         temp_next = node.next
#     #         node.val = next_node.val
#     #         next_node.val = temp_value
#     #         node.next = next_node.next
#     #         next_node.next = temp_next
#     #         node = node.next
#
#     def printlist(self):
#         node = self.main
#         while node:
#             print(node.val)
#             node = node.next
#
#
# node1 = ListNode(29)
# node2 = ListNode(31)
# node3 = ListNode(34)
# node4 = ListNode(39)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
#
# l2 = Solution()
# l2.head = node1
# # l2.swapPairs(node1)
# print(l2.printlist())
