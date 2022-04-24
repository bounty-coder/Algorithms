# Given an m x n grid of characters board and a string word,
# return true if word exists in the grid.

# The word can be constructed from letters of sequentially 
# adjacent cells, where adjacent cells are horizontally or 
# vertically neighboring. 

# The same letter cell may not be used more than once.

# Input: 
# word = "ABCCED" ,board =
#   [["A","B","C","E"],
#    ["S","F","C","S"],
#    ["A","D","E","E"]], 
# Output: true


class Solution:
    def exist(self, A: List[List[str]], B: str) -> bool:
        row,col=len(A),len(A[0])

        def dfs(i,j,k):
            if k==len(B):
                return 1
            if i>=row or j>=col or i<0 or j<0 or B[k]!=A[i][j]:
                return False
            # comment this line for same letter cell may be used more than once.
            A[i][j]="*"  
            res=dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1)
            # comment this line for same letter cell may be used more than once.
            A[i][j]=B[k]
            return res
            
        for i in range(row):
            for j in range(col):
                if A[i][j]==B[0]:
                    if dfs(i,j,0):
                        return True
        return False