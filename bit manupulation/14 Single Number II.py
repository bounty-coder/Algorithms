# Given an integer array nums where every element appears 
# three times except for one, which appears exactly once. 
# Find the single element and return it.

# Input: nums = [2,2,3,2]
# Output: 3

#approach 1 sorting
#approach 2 hashing  TC- O(n) SC-O(n)
def singleNumber( nums):
    dic={}
    for i in range(len(nums)):
        if nums[i] in dic:
            dic[nums[i]]+=1
        else:
            dic[nums[i]]=1
    nums=list(set(nums)) 
    for i in range(len(nums)):
        if dic[nums[i]]==1:
            return nums[i]


#approach 3 bit  TC- O(n) SC-O(1)
#not work for neg number
import math
def singleN(nums):
    result=0
    n=len(nums)
    k= int(math.log2(max(nums)))+1
    for i in range(k):
        sm=0
        x=(1<<i)
        for j in range(n):
            if nums[j] & x:
                sm=sm+1
        
        if sm%3!=0:
            result=result|x
    return result

nums = [2,2,3,2]
print(singleNumber(nums))