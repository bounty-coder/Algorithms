#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,arr,N):
        # code here
        s=sum(arr[0:k])
        if k>N:
            return -1
        curr=s
        for i in range(1,N-k+1):
            curr+=arr[k+i-1]-arr[i-1]
            s=max(curr,s)
        return s
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends