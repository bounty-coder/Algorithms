# You are a professional robber planning to rob houses along a street. Each house
# has a certain amount of money stashed, the only constraint stopping you from robbing
# each of them is that adjacent houses have security systems connected and it will
# automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [1,2,3,1]
# Output: 4

# Input: nums=[2,1,1,2]
# output: 4

def rob(nums):
    n=len(nums)
    if n==0:
        return 0
    if n==1:
        return nums[0]
    dp=[0 for i in range(n)]
    dp[0]=nums[0]
    dp[1]=max(nums[1],nums[0])
    
    for i in range(2,n):
        dp[i]=max(nums[i]+dp[i-2],dp[i-1])
    
    return dp[n-1]

nums=[2,1,1,2]
print(rob(nums))