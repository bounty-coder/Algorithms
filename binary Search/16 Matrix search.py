# Given a matrix of integers A of size N x M and an integer B.
# Write an efficient algorithm that searches for integar B in matrix A.

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last
#  integer of the previous row.
# Return 1 if B is present in A, else return 0.

# Input 1:
#     A = [ [1,   3,  5,  7],
#           [10, 11, 16, 20],
#           [23, 30, 34, 50]  ]
#     B = 3
# Output 1:  1

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        m=len(A)
        n=len(A[0])
        mi=A[0][0]
        ma=A[m-1][n-1]
        li=[]
        for row in A:
            li.extend(row)
        l=0
        r=len(li)-1
        while(l<=r):
            mid=l+(r-l)//2
            if(li[mid]==B):
                return 1
            elif(li[mid]<B):
                l=mid+1
            else:
                r=mid-1
        return 0