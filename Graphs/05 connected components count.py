# Given a graph with V vertices. Find the number of Provinces.
# Note: A province is a group of directly or indirectly connected
#  cities and no other cities outside of the group.

def numProvinces(self, adj, V):
    # code here 
    def dfs(V,adj,i,visited):
        visited[i]=True
        for j in range(V):
            if adj[i][j]==1 and not visited[j]:
                dfs(V,adj,j,visited)
    count=0
    visited=[False for i in range(V+1)]
    for i in range(V):
        if not visited[i]:
            dfs(V,adj,i,visited)
            count+=1
    return count