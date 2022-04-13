# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
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