# Search in Rotated Sorted Array

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# find the pivot element
# binary search on two sorted arrays
class Solution:
    def binarysearch(self,arr,start,end,k):
        while start<=end:
            mid=start+(end-start)//2
            if arr[mid]==k:
                return mid
                break
            elif arr[mid]<k:
                start=mid+1
            else:
                end=mid-1
        return -1
        
    def search(self, arr, k):
        n=len(arr)
        start,end=0,n-1
        pivot=-1    #to find where is smallest element
        if arr[0]<arr[n-1]:
            pivot=0
        else:
            while start<=end:
                if arr[start]<=arr[end]:
                    pivot=start
                    break
                mid=start+(end-start)//2
                nex=(mid+1)%n
                prev=(mid-1+n)%n
                if arr[mid]<=arr[prev] and arr[mid]<=arr[nex]:
                    pivot=mid
                    break
                if arr[start]<=arr[mid]:
                    start=mid+1
                elif arr[mid]<=arr[end]:
                    end=mid-1
        # print(pivot)
        one=self.binarysearch(arr,0,pivot-1,k)
        two=self.binarysearch(arr,pivot,n-1,k)
        # print(one,two)
        if one!=-1:
            return one
        elif two!=-1:
            return two
        else:
            return -1

a=list(map(int , input().strip().split()))
k=int(input())
ob = Solution()
ans=ob.search(a,k)
print(ans)