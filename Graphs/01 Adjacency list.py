# Given the adjacency list of a bidirectional graph. Your task is to 
# copy/clone the adjacency list for each vertex and return a new list.

# Input: 5 7 (V,E)
# [[0 1],
# [0 4],
# [1 2],
# [1 3],
# [1 4],
# [2 3],
# [3 4]]

# output: 

# 0-> 1-> 4
# 1-> 0-> 2-> 3-> 4
# 2-> 1-> 3
# 3-> 1-> 2-> 4
# 4-> 0-> 1-> 3

def printGraph(V, adj):
    path=[]
    for i in range(V):
        path.append([i]+adj[i])
    return path

# no of vertices and edges
V, E = map(int, input().split())

adj = [[] for i in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
ans = printGraph(V, adj)
for i in range(len(ans)):
    for j in range(len(ans[i])-1):
        print(ans[i][j], end = "-> ")
    print(ans[i][len(ans[i])-1]);