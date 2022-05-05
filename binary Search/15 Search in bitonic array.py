# Given a bitonic sequence A of N distinct elements, 
# write a program to find a given element B in the 
# bitonic sequence in O(logN) time.

# A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
# B = 30
# O/p 2:  -1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, arr, B):
        n=len(arr)
        start,end=0,n-1
        #findning peak
        peak=-1
        while start<=end:
            mid=(start+end)//2
            if mid>0 and mid<n-1:
                if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                    peak=mid
                    break
                elif arr[mid+1]>arr[mid] and arr[mid]>arr[mid-1]:
                    start=mid
                else:
                    end=mid  
        
        def binaryup(lst,f,l,n):
            while f<=l:
                mid =( f + l ) // 2
                if n == lst[mid]:
                    return mid
                elif n < lst[mid]:
                    l=mid-1
                elif n > lst[mid]:
                    f=mid+1
            return -1
        
        def binarydown(lst,f,l,n):
            while f<=l:
                mid =( f + l ) // 2
                if n == lst[mid]:
                    return mid
                elif n > lst[mid]:
                    l=mid-1
                elif n < lst[mid]:
                    f=mid+1
            return -1     
        x=y=-1
        x = binaryup(arr,0,peak,B)
        y = binarydown(arr,peak+1,n-1,B)
        
        if x!=-1:
            return x
        elif y!=-1:
            return y
        return -1