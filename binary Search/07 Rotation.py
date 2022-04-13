# Given an ascending sorted rotated array Arr of distinct integers of size N.
#  The array is right rotated K times. Find the value of K.

# N = 5
# Arr[] = {5, 1, 2, 3, 4}
# Output: 1

class Solution:
    def findKRotation(self,arr,  n):
        if arr[0]<arr[n-1]:
            return 0
        pivot=-1
        start,end=0,n-1
        while start<=end:
            if arr[start]<=arr[end]:
                return start
            mid=start+(end-start)//2
            nex=(mid+1)%n
            prev=(mid-1+n)%n   # +n cause if it goes into -1+n then positive number
            if arr[mid]<=arr[nex] and arr[mid]<=arr[prev]:
                pivot=mid
                break
            # move to the unsorted array
            if arr[start]<=arr[mid]:
                start=mid+1
            elif arr[mid]<=arr[end]:
                end=mid+1
        return pivot
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3


n=int(input())
a=list(map(int , input().strip().split()))
ob = Solution()
ans=ob.findKRotation(a, n)
print(ans)

