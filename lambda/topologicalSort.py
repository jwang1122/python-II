from collections import defaultdict 

def toposort(n):
    graph = defaultdict(list)
    V = n

    def topologicalSortUtil(v,visited,stack): 
        # Mark the current node as visited. 
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex 
        for i in graph[v]: 
            if visited[i] == False: 
                topologicalSortUtil(i,visited,stack) 

        # Push current vertex to stack which stores result 
        stack.append(v) 

    # The function to do Topological Sort. It uses recursive 
    # topologicalSortUtil() 
    def topologicalSort(): 
        visited = [False]*V 
        stack =[] 

        for i in range(V): 
            if visited[i] == False: 
                topologicalSortUtil(i,visited,stack) 

        return stack

stack = toposort(6)

print(stack) 