# use a queue data structure for bfs

class Solution:
    def bfsOfGraph(self, V, adj):
        # code here
        bfs=[]
        vis=[False]*V
        q=[]
        q.append(0)
        vis[0]=True
        while len(q)!=0:
            node=q.pop(0)
            bfs.append(node)
            for j in adj[node]:
                if vis[j]==False:
                    vis[j]=True
                    q.append(j)
        return bfs
        
V, E = map(int, input().split())
adj = [[] for i in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
ob = Solution()
ans = ob.bfsOfGraph(V, adj)
for i in range(len(ans)):
    print(ans[i], end = " ")
