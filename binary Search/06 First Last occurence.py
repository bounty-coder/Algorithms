# Input:
# N = 4 , X = 3
# arr[] = { 1, 3, 3, 4 }
# Output:
# 1 2
class Solution: 
    def firstAndLast(self, arr, n, x): 
        # Code here
        start,end=0,n-1
        first=-1
        while start<=end:
            mid=start+(end-start)//2
            if x==arr[mid]:
                first=mid
                end=mid-1
            elif x<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        
        last=-1
        start,end=0,n-1
        while start<=end:
            mid=start+(end-start)//2
            if x==arr[mid]:
                last=mid
                start=mid+1
            elif x<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        
        if first==-1:
            return [-1]
        return [first,last]        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input()) 
    for _ in range(t):
        n,x = [int(i) for i in input().split()] 
        arr = [int(i) for i in input().split()] 
        ob=Solution() 
        ans=ob.firstAndLast(arr,n,x) 
        s=(" ").join(map(str,ans))
        print(s)

# } Driver Code Ends