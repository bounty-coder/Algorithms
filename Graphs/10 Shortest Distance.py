# find shortest path between nodes

#  1 - 0   7 - 6
#  |   | / | / |
#  2   3 - 4 - 5

# from 2 to 6 => 5
# from 0 to 7 => 2

from collections import deque
def bfs(start,dest,adj,v):
    dist=[float("inf")]*v
    q=deque()

    dist[start]=0
    q.append(start)

    while len(q):
        node=q.popleft()
        
        for i in adj[node]:
            if dist[node]+1<dist[i]:
                dist[i]=dist[node]+1
                q.append(i)
    
    print(dist[dest])

def add_edge(adj, src, dest):
    adj[src].append(dest)
    adj[dest].append(src)


v = 8;
adj = [[] for i in range(v)];

add_edge(adj, 0, 1)
add_edge(adj, 0, 3)
add_edge(adj, 1, 2)
add_edge(adj, 3, 4)
add_edge(adj, 3, 7)
add_edge(adj, 4, 5)
add_edge(adj, 4, 6)
add_edge(adj, 4, 7)
add_edge(adj, 5, 6)
add_edge(adj, 6, 7)
source = 2
dest = 6

bfs(source,dest,adj,v)