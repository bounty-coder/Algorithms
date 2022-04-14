# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# approach
# traverse from first element bfs/dfs wise and for auxiliary space
# O(1) we can change visited 1's to 2 and if we do not want to change
# the grid we can use a visited list or set for the lookup if we had 
# visited the node or not. 

#for horizontally and vertically only (4 directions)
# approach 1 (change grid elements, O(1) extra space, dfs)
class Solution:
    
    def DFS(self,grid,i,j,m,n):
        if i>=0 and j>=0 and i<m and j<n and grid[i][j]=="1":
            grid[i][j]="2"
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                self.DFS(grid,x,y,m,n)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        island=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]=="1":
                    island+=1
                    self.DFS(grid,i,j,m,n)
                    
        return island

# for horizontally, vertically and diagonally( 8 directions)
# approach 2 (use visited array, O(n^2) space)
from collections import deque
def numIslands(grid):
    #code here
    if not grid:
        return 0
    visited=set()
    m=len(grid[0])
    n=len(grid)
    islands=0
    
    def bfs(r,c):
        q=deque([])
        visited.add((r,c))
        q.append((r,c))
        while len(q):
            # if want to convert bfs to dfs change 
            # popleft() to pop()
            row,col=q.popleft()
            directions=[[-1,0],[0,1],[1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
            for dr,dc in directions:
                r,c=row+dr,col+dc
                if (r in range(n) and c in range(m) and grid[r][c]==1 and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))
                
    for i in range(n):
        for j in range(m):
            if (grid[i][j]==1) and ((i,j) not in visited):
                bfs(i,j)
                islands+=1
    return islands