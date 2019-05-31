from collections import defaultdict, deque


class Node:
    def __init__(self, value):
        self.value = value


class Graph:
    def __init__(self, verteces_number):
        self.verteces = verteces_number + 1
        self.graph = defaultdict(list)

    def add_edge(self, src, dst):
        self.graph[src].append(dst)

    def print_graph(self):
        for i in range(self.verteces):
            verteces = ', '.join(str(_) for _ in self.graph[i])
            print('Vertex number {}'.format(i) + ' connected to ' + verteces + ' vertex(ces).')

    def breadth_first_search(self, s):
        visited = [False] * len(self.graph)
        queue = list()
        queue.append(s)
        visited[s] = True
        result = '\nBreadth First Search starting from node %s: ' % s
        while queue:
            s = queue.pop(0)
            result += str(s) + ' '
            for i in self.graph[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True
        return result

    def depth_first_search(self, start):
        visited = [False] * self.verteces
        visited[start] = True
        stack = [start]
        result = '\nDepth First Search starting from %s: ' % start
        while stack:
            node = stack.pop()
            result += str(node) + ' '
            for i in self.graph[node]:
                if visited[i] is False:
                    stack.append(i)
                    visited[i] = True
        return result


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 0)
g.add_edge(4, 1)
g.print_graph()
g.breadth_first_search(4)

h = Graph(8)
h.add_edge(0, 1)
h.add_edge(0, 2)
h.add_edge(1, 3)
h.add_edge(1, 4)
h.add_edge(1, 5)
h.add_edge(3, 4)
h.add_edge(4, 5)
h.add_edge(5, 1)
h.add_edge(5, 6)
h.add_edge(2, 6)
h.add_edge(2, 7)
h.add_edge(2, 8)
h.add_edge(6, 7)
h.add_edge(7, 8)
h.add_edge(8, 2)
h.add_edge(8, 0)
h.print_graph()
print(h.breadth_first_search(3))
print(h.depth_first_search(0))


