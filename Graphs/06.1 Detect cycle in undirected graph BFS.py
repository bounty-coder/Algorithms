# detect cycle using bfs in undirected graph 

# We do a BFS traversal of the graph. For every visited vertex ‘v’,
#  if there is an adjacent ‘u’ such that u is already visited and
#  u is not a parent of v, then there is a cycle in the graph. If
#  we don’t find such an adjacent for any vertex, 
# we say that there is no cycle. 
# We use a parent array to keep track of the parent vertex for a 
# vertex so that we do not consider the visited parent as a cycle. 

from collections import deque

class Solution:
    def bfsutil(self,i,V,adj,vis):
        parent=[-1]*V
        q=deque([])
        q.append(i)
        vis[i]=True
        while len(q):
            node=q.popleft()

            for z in adj[node]:
                
                if not vis[z]:
                    vis[z]=True
                    q.append(z)
                    parent[z]=node
                # parent of node have already value means it is already visited
                elif parent[node]!=z:
                    return True
        return False

    def isCycle(self, V, adj):
        vis=[False]*V

        #iterating over all the vertices.
        for i in range(V):

            # if vertex is not visited, we call the function to detect cycle.
            if not vis[i]:

                #if cycle is found, we return true.
                if self.dfsutil(i,V,adj,vis):
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