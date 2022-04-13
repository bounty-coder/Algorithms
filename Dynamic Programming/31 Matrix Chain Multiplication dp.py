# Input: N = 5
# arr = {40, 20, 30, 10, 30}
# Output: 26000

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    t = [[0 for x in range(n)] for x in range(n)]
  
    # t[i, j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
  
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        t[i][i] = 0
  
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L + 1):
            j = i + L-1
            t[i][j] = float("inf")
            for k in range(i, j):
                # cost / scalar multiplications
                t[i][j] = min(t[i][j],t[i][k] + t[k + 1][j] + p[i-1]*p[k]*p[j])
  
    return t[1][n-1]
  
# Driver program to test above function
arr = [10, 30, 5, 60]
size = len(arr)
  
print("Minimum number of multiplications is " +
       str(MatrixChainOrder(arr, size)))