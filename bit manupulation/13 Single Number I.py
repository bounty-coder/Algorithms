# Given a non-empty array of integers nums, every element appears
#  twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity
#  and use only constant extra space.


class Solution:
    def singleNumber(self, nums) :
        one=nums[0]
        for i in range(1,len(nums)):
            one=one^nums[i]
        return one