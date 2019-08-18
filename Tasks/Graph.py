from collections import defaultdict


class Node:
    def __init__(self, val):
        self.val = val


class Graph:
    def __init__(self):
        self.vertexes = []
        self.graph = defaultdict(list)

    def add_edge(self, src: Node, dst: Node) -> None:
        self.graph[src].append(dst)

    def traverse(self):
        for node in self.graph:
            vertexes = []
            for i in self.graph[node]:
                vertexes.append(i.val)
            print(f'Node {node.val} has vertexes {vertexes}')

    def remove_inappropriate_edges(self):
        seen = []
        for node in self.graph:
            for v in self.graph[node]:
                if v.val in seen:
                    idx = self.graph[node].index(v)
                    self.graph[node].pop(idx)
                else:
                    seen.append(v.val)



n7 = Node(7)
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2)
n1 = Node(1)

n8 = Node(8)

t = Graph()
t.add_edge(n1, n5)
t.add_edge(n1, n2)
t.add_edge(n2, n3)
t.add_edge(n2, n4)
t.add_edge(n2, n5)
t.add_edge(n5, n6)
t.add_edge(n5, n7)
t.add_edge(n5, n8)
t.add_edge(n3, n8)

print(t.traverse())
t.remove_inappropriate_edges()
print(t.traverse())
