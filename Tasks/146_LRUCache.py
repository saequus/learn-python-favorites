class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.record = {}
        self.position = {}
        self.capacity = capacity

    def update_order(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        return node

    def get(self, key: int) -> int:
        if key in self.record:
            self.position[key] = self.update_order(self.position[key])
            return self.record[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.record:
            self.record[key] = value
            node = self.position[key]
            node = self.update_order(node)
            node.val = value
        else:
            if self.size == self.capacity:
                self.record.pop(self.head.next.key, None)
                self.position.pop(self.head.next.key, None)

                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next

                self.size -= 1

            node = Node(key, value)
            node.prev = self.tail.prev
            node.next = self.tail

            self.tail.prev.next = node
            self.tail.prev = node
            self.position[key] = node
            self.record[key] = value
            self.size += 1
