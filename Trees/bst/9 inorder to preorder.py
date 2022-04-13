class Solution:
    
    def solve(self,nums,ls,s,e):
        if s>e:
            return 
        mid=(s+e)//2
        temp=nums[mid]
        ls.append(temp)
        self.solve(nums,ls,s,mid-1)
        self.solve(nums,ls,mid+1,e)

    def sortedArrayToBST(self, nums):
    	    # code here
        ls=[]
        s=0
        e=len(nums)-1
        self.solve(nums,ls,s,e)
        return ls
        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends