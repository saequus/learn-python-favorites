

#
# class ListNode(object):
#     def __init__(self, val, next_node=None):
#         self.val = val
#         if next_node:
#             self.next = next_node
#         else:
#             self.next = None
#
#     def traverse(self):
#         node = self
#         while node:
#             print(node.val)
#             node = node.next
#
#
# class SpecialList(object):
#     def __init__(self):
#         self.head = ListNode
#
#     def printList(self):
#         node = self.head
#         while node:
#             print(node.val)
#             node = node.next
#
#     def addMiddle(self, before, value):
#         node = self.head
#         newNode = ListNode(value)
#         while node:
#             if node.next == before:
#                 node.next = newNode
#                 newNode.next = before
#             node = node.next
#
#     def addAfter(self, value):
#         newNode = ListNode(value)
#         node = self.head
#         while node:
#             if node.next == None:
#                 node.next = newNode
#                 break
#             node = node.next
#
#     def removeFromEnd(self, nth):
#         node = self.head
#         all = 0
#         curr = 0
#         while node:
#             all += 1
#             node = node.next
#         pos = all - nth
#         node = self.head
#         while node:
#             curr += 1
#             if curr == pos and node.next.next:
#                 node.next = node.next.next
#             node = node.next

#
# node4 = ListNode(8)
# node3 = ListNode(6, node4)
# node2 = ListNode(5, node3)
# node1 = ListNode(2, node2)
#
# print(node1.traverse())
# l1 = SpecialList()
# l1.head = node1
# l1.addMiddle(node3, 100)
# l1.addAfter(200)
# print(l1.printList())
# l1.removeFromEnd(4)
# print(l1.printList())
#
#


