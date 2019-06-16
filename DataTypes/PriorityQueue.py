import heapq
from queue import PriorityQueue

# Priority Queue is an extension of the queue with following properties.
# 1) An element with high priority is dequeued before an element with low
# priority.
# 2) If two elements have the same priority, they are served according to their
# order in the queue.


# from GeekForGeeks

class SelfDefinedPriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max_num = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_num]:
                    max_num = i
            item = self.queue[max_num]
            del self.queue[max_num]
            return item
        except IndexError:
            print()
            exit()


x = SelfDefinedPriorityQueue()
x.insert(3)
x.insert(12)
x.insert(15)
print('SelfDefinedPriorityQueue')
print('full queue:', x)
x.delete()
print('deleted last item, queue:', x)
while not x.is_empty():
    x.delete()
print('empty queue:', x)
print('– – – – - – – –')


# with heapq realisation

q = []

heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

print('Realisation from heapq module')
while q:
    next_item = heapq.heappop(q)
    print(next_item)
print('- – – – – –')

# with queue.PriorityQueue

q = PriorityQueue()
q.put((2, 'go'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

print('Realisation with queue.PriorityQueue')
while not q.empty():
    next_item = q.get()
    print(next_item)
print('- – – – – –')
