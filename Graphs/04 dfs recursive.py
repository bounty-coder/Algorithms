# Input:
# 5 4 (V and E)
# 0 1 
# 0 2
# 0 3 
# 2 4

# output: 0 1 2 4 3
# TC- O(N+E)     SC- O(N)+O(N) (vis arr+ adj list)

#Function to return a list containing the DFS traversal of the graph.
def DFSrecur(v,adj,vis,graph):
    vis.add(v)
    graph.append(v)
    for i in adj[v]:
        if i not in vis:
            DFSrecur(i,adj,vis,graph)

def dfsOfGraph( V, adj):
    # code here
    vis=set()
    graph=[]
    DFSrecur(0,adj,vis,graph)
    return graph

# V- total no of vertices
# E- no of Edges
V,E=map(int,input().split())
# adj is a collection of all the edge between two nodes u and v 
adj=[[] for i in range(V+1)]
for i in range(E):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

ans=dfsOfGraph(V,adj)
for i in range(len(ans)):
    print(ans[i],end=" ")
print()
