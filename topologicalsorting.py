from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  #dictionary containing adjacency List
        self.V = vertices  #No. of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        if self.isCyclic():
            return []
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        return stack

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(2, 0)
print("57",g.topologicalSort())

g = Graph(4)
g.addEdge(3, 2)
g.addEdge(3, 1)
g.addEdge(2, 0)
g.addEdge(1, 0)
print("64:",g.topologicalSort())

g = Graph(4)
g.addEdge(1, 3)
g.addEdge(3, 1) # circle graph
g.addEdge(2, 0)
g.addEdge(1, 0)
print("71: Circle Graph=>",g.topologicalSort())

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(1, 5) # circle graph
print("81: Circle Graph=>",g.topologicalSort())

g = Graph(2)
g.addEdge(1,0)
print("85:",g.topologicalSort())