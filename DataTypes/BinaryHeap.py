from heapq import heappush, heappop, heapify


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap
# heapify - transform list into heap, in place, in linear time

class MinHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    def insert_key(self, k):
        heappush(self.heap, k)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = \
                self.heap[self.parent(i)], self.heap[i]

    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

        # Get the minimum element from the heap

    def get_min(self):
        return self.heap[0]


heap_object = MinHeap()
heap_object.insert_key(3)
heap_object.insert_key(2)
heap_object.delete_key(1)
heap_object.insert_key(15)
heap_object.insert_key(5)
heap_object.insert_key(4)
heap_object.insert_key(45)

print(heap_object.extract_min())
print(heap_object.get_min())
heap_object.decrease_key(2, 1)
print(heap_object.get_min())
