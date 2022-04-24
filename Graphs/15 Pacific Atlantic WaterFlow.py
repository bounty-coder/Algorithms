# There is an m x n rectangular island that borders both the Pacific Ocean 
# and Atlantic Ocean. The Pacific Ocean touches the island's left and top 
# edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island receives a lot of rain, and the rain water can flow to 
# neighboring cells directly north, south, east, and west if the 
# neighboring cell's height is less than or equal to the current cell's
# height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
#  denotes that rain water can flow from cell (ri, ci) 
# to both the Pacific and Atlantic oceans.

# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pacific,atlantic=set(),set()
        
        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or
               r<0 or c<0 or r==rows or c==cols or heights[r][c]<prevHeight):
                return 
            visit.add((r,c))
            dfs(r+1 , c ,visit, heights[r][c])
            dfs(r , c+1 ,visit, heights[r][c])
            dfs(r-1 , c ,visit, heights[r][c])
            dfs(r , c-1 ,visit, heights[r][c])
        
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])
        
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
            
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res