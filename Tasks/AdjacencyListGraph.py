class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, verteces):
        self.V = verteces
        self.graph = self.V * [None]

    def add_edge(self, src, dst):
        node = Node(dst)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dst]
        self.graph[dst] = node

    def print_graph(self):
        for i in range(self.V):
            print('Adj vertex {}'.format(i), end='')
            temp = self.graph[i]
            while temp:
                print(' --> {}'.format(temp.vertex), end='')
                temp = temp.next
            print('\n')


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.print_graph()




