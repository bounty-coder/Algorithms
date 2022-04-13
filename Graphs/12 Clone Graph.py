# Clone an undirected graph. Each node in the graph contains 
# a label and a list of its neighbors.

#approach 
# traverse the graph using dfs or bfs and create new nodes of each
# new traversed node's value. 
# Use a hashmap where old node maps to new nodes(copy nodes).
# only copying node is not sufficient, we also have to link nodes
# both sides as it is an undirected graph.
# so traversing dfs and append child node to node using recursion

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        oldtonew={}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]

            newnode=UndirectedGraphNode(node.label)
            oldtonew[node]=newnode
            for nei in node.neighbors:
                newnode.neighbors.append(dfs(nei))
            return newnode
        
        return dfs(node) if node else None