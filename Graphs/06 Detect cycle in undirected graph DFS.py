# Given an undirected graph with V vertices and E edges, 
# check whether it contains any cycle or not. 

#input-
# 5 5 (V, E)
# 0 4
# 1 2
# 1 4
# 2 3
# 3 4

#o/p- 1

# Run a DFS from every unvisited node. Depth First Traversal can be
# used to detect a cycle in a Graph. DFS for a connected graph 
# produces a tree. There is a cycle in a graph only if there is a 
# back edge present in the graph.
# To find the back edge to any of its ancestors keep a visited array
#  and if there is a back edge to any visited node then
#  there is a loop and return true.

class Solution:
    def dfsutil(self,i,parent,adj,vis):

        #marking the current vertex as visited.
        vis[i]=True

        #iterating on all the adjacent vertices.
        for z in adj[i]:

            # if node is equal to parent then skip
            if z==parent:
                continue

            #if current vertex is visited, we return true
            elif vis[z]:
                return True

			#else we call the function recursively to detect the cycle.
            elif self.dfsutil(z,i,adj,vis):
                return True
        return False

    #solution function
    def isCycle(self, V, adj):
        vis=[False]*V

        #iterating over all the vertices.
        for i in range(V):

            # if vertex is not visited, we call the function to detect cycle.
            if not vis[i]:

                #if cycle is found, we return true.
                if self.dfsutil(i,-1,adj,vis):
                    return True
        return False

V, E = map(int, input().split())
adj = [[] for i in range(V)]


for _ in range(E):
    u, v = map(int, input().split())
    # converting into graph
    adj[u].append(v)
    adj[v].append(u)
obj = Solution()
ans = obj.isCycle(V, adj)
if(ans):
    print("1")
else:
    print("0")