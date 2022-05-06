# Given an integer K and an array, height[] where height[i]
# denotes the height of the ith tree in a forest. The task 
# is to make a cut of height X from the ground such that 
# exactly K unit wood is collected. If it is not possible, 
# then print -1 else print X.

#  A = [4, 42, 40, 26, 46]
#  B = 20
# Op 2: 36
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        def woodcut(A,mid):
            s=0
            for i in range(len(A)):
                if A[i]>=mid:
                    s+=A[i]-mid
            return s

        start,end=0,max(A)

        while start<=end:
            mid=(start+end)//2
            x=woodcut(A,mid)
            if x==B or start==mid:
                return mid
            elif x>B:
                start=mid
            else:
                end=mid
        
        return mid