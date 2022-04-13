class Solution:
    
    #Function to detect cycle in a directed graph.
    def cyclecheck(self,node,adj,vis,dfs_vis):
        # Mark current node as visited and
        # adds to recursion stack
        vis[node]=True
        dfs_vis[node]=True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for z in adj[node]:
            if not vis[z]:
                if self.cyclecheck(z,adj,vis,dfs_vis):
                    return True
            elif dfs_vis[z]:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        dfs_vis[node]=False
        return False
            
    def isCyclic(self, V, adj):
        # code here
        vis=[False]*V
        dfs_vis=[False]*V
        
        for i in range(V):
            if not vis[i]:
                if self.cyclecheck(i,adj,vis,dfs_vis):
                    return True
        return False
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
V,E = list(map(int, input().strip().split()))
adj = [[] for i in range(V)]
for i in range(E):
    a,b = map(int,input().strip().split())
    adj[a].append(b)
ob = Solution()

if ob.isCyclic(V, adj):
    print(1)
else:
    print(0)
