"""
could not handle circle graph
"""
from dataclasses import dataclass, field
from collections import deque

@dataclass
class Graph :

    nodes : int
    adjlist : dict = field(default_factory = dict)                 # Stores the graph in an adjacency list
    incoming_edge_count : list = field(default_factory = list)     # For a node, it stores the number of incoming edges. 
    topo_order : list = field(default_factory = list)              # Stores the nodes in lexical topologically sorted order.
    zero_incoming_edge_node : list = field(default_factory = list) # Stores the nodes that have zero incoming edges.
    
    # Create an adjacency list for storing the edges
    def addEdge(self, src, dst) :

        if src not in self.adjlist :
           self.adjlist[src] = []
        self.adjlist[src].append(dst)

        self.incoming_edge_count[dst] += 1

    def topologicalSort(self) :

        for node in range(self.nodes) :
            if self.incoming_edge_count[node] == 0 :
               self.zero_incoming_edge_node.append(node)

        while self.zero_incoming_edge_node :
            self.zero_incoming_edge_node.sort()
            src = self.zero_incoming_edge_node.pop(0)

            # Iterate through the adjacency list
            if src in self.adjlist :
                for node in self.adjlist[src] :
                    self.incoming_edge_count[node] -= 1
                    if self.incoming_edge_count[node] == 0 :
                        self.zero_incoming_edge_node.append(node)

            self.topo_order.append(src)

        return self.topo_order

def main() :

    node_cnt = 7
    g = Graph(node_cnt)
    g.incoming_edge_count = [0] * node_cnt # For a node, it stores the number of incoming edges.

    g.addEdge(0,2);
    g.addEdge(0,5);
    g.addEdge(1,3);
    g.addEdge(1,6);
    g.addEdge(2,4);
    g.addEdge(3,5);
    g.addEdge(5,2);
    g.addEdge(5,4);
    g.addEdge(6,2);

    print("59:",g.topologicalSort())

    g = Graph(4)
    g.incoming_edge_count = [0] * 4 # For a node, it stores the number of incoming edges.
    g.addEdge(1, 3)
    g.addEdge(3, 1)
    g.addEdge(2, 0)
    g.addEdge(1, 0)
    print("66:",g.topologicalSort())

    g = Graph(6)
    g.incoming_edge_count = [0] * 6 # For a node, it stores the number of incoming edges.
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(1, 5)
    print("76:",g.topologicalSort())

    g = Graph(2)
    g.incoming_edge_count = [0] * 2 # For a node, it stores the number of incoming edges.
    g.addEdge(1,0)
    print("80:",g.topologicalSort())

if __name__ == "__main__" :
    main()