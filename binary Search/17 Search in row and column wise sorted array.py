# Given a matrix mat[][] of size N x M, where every row and
# column is sorted in increasing order, and a number X is given. 
# The task is to find whether element X is present in the matrix or not.

# Input:  N = 3, M = 3
# mat[][] = 3 30 38 
#          44 52 54 
#          57 60 69
# X = 62
# Output:  0

# Input: N = 1, M = 6
# mat[][] = 18 21 27 38 55 67
# X = 55
# Output: 1

class Solution:
    def matSearch(self,A, m, n, B):
        i=0
        j=n-1
        while i>=0 and i<m and  j>=0 and j<n:
            if A[i][j]==B:
                return 1
            elif A[i][j]>B:
                j-=1
            elif A[i][j]<B:
                i+=1
            
        return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))