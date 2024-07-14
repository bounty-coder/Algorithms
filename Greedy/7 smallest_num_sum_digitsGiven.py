# https://www.geeksforgeeks.org/problems/smallest-number5829/1

# Given two integers s and d. The task is to find the smallest number such that the
# sum of its digits is s and the number of digits in the number are d. 
# Return a string that is the smallest possible number. If it is not possible then return -1.

# Input: s = 9, d = 2
# Output: 18 
# Explanation: 18 is the smallest number possible with the sum of digits = 9 and total digits = 2.


#Method - Greedy approach
# take a list of digit d, make first element as 1 an the start from last and start assigning 9
# if assiginign 9, reduce 9 from sum. If less than 9, then do appropriate accordingly
class Solution:
    def smallestNumber(self, s, d):
        # If sum is greater than 9*digits, we can never chase the sum, not possible
        if s>9*d:
            return -1

        ls=[0]*d
        ls[0]=1
        s-=1
        while d>1:
            if s>9:
                ls[d-1]=9
            else:
                ls[d-1]=s
            s-=ls[d-1]
            if s==0:
                break
            d-=1
        if d==1:
            ls[0]+=s
        return int("".join([str(i) for i in ls]))
