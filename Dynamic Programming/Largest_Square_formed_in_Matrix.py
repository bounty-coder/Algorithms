# Given a binary matrix mat of size n * m, find out the maximum length of a side of a square sub-matrix with all 1s.
'''
Input: n = 6, m = 5
mat = [[0, 1, 1, 0, 1], 
       [1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]
Output: 3
'''


from typing import List
'''
What is our intent?
1)    The first thing came to mind was like can we apply DFS here? But it will be very complecated as well as time consuming
2)    We can apply DP here, How?
        if mat[i][j]==1, then check for down, right and down-right element if they all are 1 then increase the value of down-right to 2(for dp table)
'''

class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        dp = [[0 for i in range(m+1)]for j in range(n+1)]
        res=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if mat[i-1][j-1]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    res=max(res,dp[i][j])
        return res
