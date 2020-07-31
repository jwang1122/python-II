class Node:
    def __init__(self, id):
        self.id = id
        self.prerequests = []

    def addPrerequests(self, id):
        self.prerequests.append(id)
    
    def getPrerequests(self):
        return self.prerequests

class Main:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        noRequires = []
        node2 = list(map(lambda x: Node(x), range(n)))
        nodes = list(map(lambda x: Node(x), range(n)))
        for x in edges:
            nodes[x[1]].addPrerequests(x[0])
            node2[x[0]].addPrerequests(x[1])
            print(nodes[x[1]].getPrerequests())
        for x in nodes:
            if len(x.getPrerequests())==0:
                noRequires.append(x)


l1 = [[3, 1], [3, 2], [1, 0], [2, 0]]
main = Main(4, l1)

