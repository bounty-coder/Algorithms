# A Bipartite Graph is a graph whose vertices can be divided into two independent sets
# there is no edge that connects vertices of same set.
# A bipartite graph is possible if the graph coloring is possible using
# two colors such that vertices in a set are colored with the same color.

# It is not possible to color a cycle graph with odd cycle using two colors. 
# if graph has odd length cycle, then not bipartite else bipartite.

#Approach
# check for every node(if components are disconnected)
# traverse every node by bfs and mark color not equal to node
# if any child node is previsited and have same color as node 
# then false( is not bipartite) else true

from collections import deque
class Solution:
    def isBipartite(self,V,adj):
        is_bipartite=True
        q=deque()
        color=[-1 for i in range(V)]
        for i in range(V):
            if color[i]==-1:
                q.append(i)
                color[i]=0
                while len(q):
                    node=q.pop()
                    for z in adj[node]:
                        if color[z]==-1:
                            color[z]=color[node]^1
                            q.append(z)
                        else:
                            is_bipartite=is_bipartite & (color[z]!=color[node])
        return is_bipartite                    
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends