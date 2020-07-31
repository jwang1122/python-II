"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edge

while S is not empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S

if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)
"""


def getCourses(n, l1, s):
    l = []
    for i in l1:
        for j in l1:
            if i[0]==j[1] and i[1]==j[0]:
                return l
    while len(s) > 0 or len(l1)>0:
        if(len(s)>0):
            x = s.pop()
            l.insert(0, x)
        for i in l1:
            y = i
            removeNoEdge(y, l1)
            if (noIncomingEdge(y[1], l1)):
                s.append(y[1])
    return l


def removeNoEdge(edge, l1):
    flag = True
    for x in l1:
        if (edge[0] == x[1] and edge[1] != x[0]):
            flag = False
            break
    if flag:
        l1.remove(edge)


def noIncomingEdge(m, l):
    for x in l:
        if x[1] == m:
            return False
    return True


def findNoEdge(n, l):
    l1 = []
    for i in range(n):
        flag = True
        for x in l:
            if i == x[1]:
                flag = False
                break
        if flag:
            l1.append(i)
    return l1


if __name__ == "__main__":
    # l1 = [[3,1],[3,2],[1,0],[2,0]]
    # l2 = findNoEdge(4,l1)
    # print("093:",list(l2))

    # n = 1
    # l1 = [[1, 0]]
    # s = findNoEdge(n + 1, l1)
    # l2 = getCourses(n, l1, s)
    # print("099:",l2)

    n = 3
    l1 = [[3, 1], [3, 2], [1, 0], [2, 0]]
    s = findNoEdge(n + 1, l1)
    l2 = getCourses(n, l1, s)
    print("105:",l2)

    # n = 3
    # l1 = [[1, 0], [2, 0],[3, 1], [3, 2]]
    # s = findNoEdge(n + 1, l1)
    # l2 = getCourses(n, l1, s)
    # print("111:",l2)

    # n = 3
    # l1 = [[2, 0], [1, 0], [3, 2], [3, 1]]
    # s = findNoEdge(n + 1, l1)
    # l2 = getCourses(n, l1, s)
    # print("117:",l2)

    # n = 3
    # l1 = [[1, 0], [2, 0], [3, 2], [3, 1]]
    # s = findNoEdge(n + 1, l1)
    # l2 = getCourses(n, l1, s)
    # print("117:",l2)

    # n = 3
    # # invalid edge
    # l1 = [[1, 0], [2, 0], [3, 1], [1, 3]]
    # s = findNoEdge(n + 1, l1)
    # l2 = getCourses(n, l1, s)
    # print("124:",l2)

    # n = 5
    # l1 = [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]
    # s = findNoEdge(n + 1, l1)
    # l2 = getCourses(n, l1, s)
    # print("136:",l2)
    
    print("Done.")