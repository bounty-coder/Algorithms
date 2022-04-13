# Topological sorting in graph is a linear ordering of vertices such
# that for every directed edge u v, vertex u comes before v in the ordering.

# only possible for DAG (directed acyclic graphs)

#  2  -> 3  -> 1
#  |^          |^
#  5  -> 0  <- 4 

# op- 5 4 2 3 1 0 

#approach
# similar to dfs traversal. We can modify DFS to find Topological Sorting.
# In DFS, we start from a vertex, we first print it and then recursively 
# call DFS for its adjacent vertices. 
# But in Topological sorting. We will also use a stack. We don’t print the
# vertex immediately, we first recursively call topological sorting for
# all its adjacent vertices, then push it to a stack.

# TC- O(N+E)  SC-O(N)
class Solution:
    #Function to return list containing vertices in Topological order.
    def dfsutil(self,node,adj,vis,stack):
        vis[node]=True
        for z in adj[node]:
            if not vis[z]:
                self.dfsutil(z,adj,vis,stack)
        stack.append(node)
        
                
    def topoSort(self, V, adj):
        # Code here
        vis=[False]*V
        stack=[]
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(V):
            if not vis[i]:
                self.dfsutil(i,adj,vis,stack)
        rev=stack[::-1]
        return rev

#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


e,N = list(map(int, input().strip().split()))
adj = [[] for i in range(N)]

for i in range(e):
    u,v=map(int,input().split())
    adj[u].append(v)
    
ob = Solution()

res = ob.topoSort(N, adj)

if check(adj, N, res):
    print(1)
else:
    print(0)
