# Given a 2D binary matrix A of size  N x M  find the
#  area of maximum size square sub-matrix with all 1's.
# Input 1: 
# A =  [  [0, 1, 1, 0, 1],
#         [1, 1, 0, 1, 0],
#         [0, 1, 1, 1, 0],
#         [1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0] ]

# Output 1:  9

# Approach 1: DFS TC-O(nm)^2
#  len(row)=len(col)=len(diag)
# make calls in 3 directions passing approproate variables& flags
# along with the current length of the matrix which we have found
# as soon as hit zero return back to collar

# Approach 2: DP
def maxSizeSquare(A):
    n = len(A)
    m = len(A[0])
    dp = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        dp[i][0] = A[i][0]
    for j in range(m):
        dp[0][j] = A[0][j]

    for i in range(1, n):
        for j in range(1, m):
            if A[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i
                               - 1][j - 1])) + 1
    maxe = 0
    for i in range(n):
        for j in range(m):
            maxe = max(maxe, dp[i][j])
    return maxe * maxe