class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_empty_list(self, val: int) -> None:
        if self.head is None:
            node = ListNode(val)
            self.head = node
            self.tail = node
        else:
            print("The list isn't empty")

    def insert_at_start(self, val: int) -> None:
        if self.head is None:
            node = ListNode(val)
            self.head = node
            self.tail = node
            return
        node = ListNode(val)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_end(self, val: int) -> None:
        if self.head is None:
            node = ListNode(val)
            self.head = node
            self.tail = node
            return
        node = ListNode(val)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert_after_item(self, val: int, new_val: int) -> None:
        node = self.head
        while node.val != val:
            node = node.next
            if node is None:
                print('Node with such value has not been found. List ended')
                return
        new_node = ListNode(new_val)
        new_next = node.next
        new_prev = new_next.prev
        node.next = new_node
        new_node.next = new_next
        new_node.prev = new_prev
        new_next.prev = new_node

    def insert_before_item(self, val: int, new_val: int) -> None:
        node = self.tail
        while node.val != val:
            node = node.prev
            if node is None:
                print('Node with such value has not been found. List ended')
                return
        new_node = ListNode(new_val)
        new_prev = node.prev
        new_prev.next = new_node
        new_node.prev = new_prev
        new_node.next = node
        node.prev = new_node

    def delete_at_start(self) -> None:
        if self.head is None:
            print('List is empty. Cannot delete node for empty list')
            return
        if self.head.next is None:
            self.head = None
            return
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head

    def delete_at_end(self) -> None:
        if self.tail is None:
            print('List is empty. Cannot delete node for empty list')
            return
        if not self.tail.prev:
            self.tail = None
            return
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail

    def delete_by_value(self, val: int) -> None:
        if not self.head:
            print('List is empty. Cannot delete node for empty list')
            return
        node = self.head
        while node.val != val:
            node = node.next
            if node is None:
                print('Node with such value has not been found. List ended')
                return
        new_prev = node.prev
        new_next = node.next
        new_prev.next = new_next
        new_next.prev = new_prev

    def traverse_forwards(self) -> list:
        ans = []
        node = self.head
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    def traverse_backwards(self) -> list:
        ans = []
        node = self.tail
        while node:
            ans.append(node.val)
            node = node.prev
        return ans

    def reverse(self) -> None:
        if not self.head:
            print('List is empty.')
            return
        prev = self.head
        node = prev.next
        prev.next = None
        prev.prev = node
        while node:
            node.prev = node.next
            node.next = prev
            prev = node
            node = node.prev
        self.head, self.tail = self.tail, self.head

    def move_to_end(self, val: int) -> None:
        if not self.head:
            print('Empty list')
            return
        node = self.head
        while node.val != val:
            if node is None:
                print('No such node.')
                return
            node = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail
        self.tail.next = node
        node.next = None
        self.tail = node


l = DoubleLinkedList()
l.insert_in_empty_list(0)
l.insert_at_start(1)
l.insert_at_start(2)
l.insert_at_start(3)
l.insert_at_start(4)
l.insert_at_start(5)
l.insert_at_end(10)
l.insert_at_end(11)
l.insert_at_end(12)
l.insert_after_item(0, 8)
l.insert_after_item(8, 9)
l.insert_before_item(8, 7)
l.insert_before_item(7, 6)
print(l.traverse_forwards())
print(l.traverse_backwards())
l.delete_at_end()
l.delete_at_start()
print(l.traverse_forwards())
print(l.traverse_backwards())
l.delete_by_value(7)
l.delete_by_value(3)
print(l.traverse_forwards())
print(l.traverse_backwards())
l.reverse()
print('reverse list')
print(l.traverse_forwards())
print(l.traverse_backwards())
print('move 10 to the end')
l.move_to_end(10)
print(l.traverse_forwards())
print(l.traverse_backwards())

