# A Bitonic Sequence is a sequence of numbers that is first 
# strictly increasing then after a point decreasing.
# find peak index


# Input: arr = [0,10,5,2]
# Output: 1

class Solution:
    def peakIndexInMountainArray(self, arr):
        n=len(arr)
        start,end=0,n-1
        while start<=end:
            mid=(start+end)//2
            if mid>0 and mid<n-1:
                if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                    return mid
                elif arr[mid-1]>arr[mid]:
                    end=mid-1
                else:
                    start=mid+1
            elif mid==0:
                if arr[0]>arr[1]:
                    return 0
                else:
                    return 1
            elif mid==n-1:
                if arr[n-1]>arr[n-2]:
                    return n-1
                else:
                    return n-2