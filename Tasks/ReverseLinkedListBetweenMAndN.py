class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        self.head = head

    def traverse(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def reverseList2(self, head, m, n):
        if not head:
            return None

        first = ListNode(0)
        first.next = head
        prev = first

        for i in range(m - 1):
            prev = prev.next

        curr = prev.next
        post = curr.next
        for i in range(n - m):
            curr.next = post.next
            post.next = prev.next
            prev.next = post
            post = curr.next
        return first.next

# 1 1 1
# 2 2 2
# 3 4 5
# 4 3 4
# 5 5 3
# 6 6 6


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8


f = Solution(n1)
print(f.traverse())
f.reverseList2(n1, 2, 6)
print(f.traverse())
print("- - - -")

