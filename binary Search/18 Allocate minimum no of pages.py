# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1/#

# You are given N number of books. Every ith book has Ai number of pages.
# You have to allocate contiguous books to M number of students.
# There can be many ways or permutations to do so. In each permutation,
# one of the M students will be allocated the maximum number of pages.
#  Out of all these permutations, the task is to find that particular
#  permutation in which the maximum number of pages allocated to a 
# student is the minimum of those in all the other permutations and
#  print this minimum value.

# N = 4
# A[] = {12,34,67,90}
# M = 2
# Output:113
# Explanation
# {12} and {34, 67, 90} Maximum Pages = 191
# {12, 34} and {67, 90} Maximum Pages = 157
# {12, 34, 67} and {90} Maximum Pages =113.

# Approach 1: BRuteforce
# Approach 2:
#  We have to minimise the maximum no of pages allocated
# So, maximum no of pages one student can read= sum of array(all allocated to him)
# Similarly, minimum will be 0. This will be the range. Given that 
# atleast 1 book will be allocated to each student. 
# we need to check if we can assign pages to all students in
# a way that the maximum number doesn’t exceed current value.
#  To do this, we sequentially assign pages to every student 
# while the current number of assigned pages doesn’t exceed 
# the value. In this process, if the number of students becomes
#  more than m, then the solution is not feasible. Else feasible.

class Solution:
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        def isvalid(A,N,M,mx):
            if N<M:
                return False
            student=1
            s=0
            for i in range(N):
                s+=A[i]
                if s>mx:
                    student+=1
                    s=A[i]
                if student>M:
                    return False
            return True
        
        # We can apply BS even on unsorted A cause we are applying
        # BS on range not on A
        # first use start=0 (improvement max(A))
        # cause it will be more near to avg and all minimum
        start=max(A)  
        end=sum(A)
        res=-1
        while start<=end:
            mid=(start+end)//2
            # If a current mid can be a solution, then we search 
            # on the lower half, else we search in higher half.
            if isvalid(A,N,M,mid):
                res=mid
                end=mid-1
            else:
                start=mid+1
        
        return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends