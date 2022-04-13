
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        dfs=[]
        visited=[False for i in range(V)]
        stack=[]
        stack.append(0)
        while len(stack):
            node=stack.pop()
            
            if not visited[node]:
                dfs.append(node)
                visited[node]=True
            
            for i in reversed(adj[node]):
                if not visited[i]:
                    stack.append(i)
        return dfs

#{ 
#  Driver Code Starts

V,E=map(int,input().split())
adj=[[] for i in range(V+1)]
for i in range(E):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
ob=Solution()
ans=ob.dfsOfGraph(V,adj)
for i in range(len(ans)):
    print(ans[i],end=" ")
print()
