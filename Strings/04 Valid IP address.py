# A valid IP address consists of exactly four integers separated
# by single dots. Each integer is between 0 and 255 (inclusive)
# and cannot have leading zeros.

# Given a string s containing only digits, return all possible
#  valid IP addresses that can be formed by inserting dots into s.
#  You are not allowed to reorder or remove any digits in s. You
#  may return the valid IP addresses in any order.

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# soln1- bruteforce  O(N^3),O(1)
# Split the string with ‘ . ‘ and then check for all corner cases.
# Before entering the loop, check the size of the string. Generate
# all the possible combinations using looping through the string.
# If IP is found to be valid then return the IP address, else
# simply return the empty list.

#soln2- Recursion

class Solution:
    def restoreIpAddresses(self, A: str) -> List[str]:
        res=[]
        if len(A)>12 or len(A)<4:
            return res
        
        def backtrack(i,dots,curIP):
            if dots==4 and i==len(A):
                res.append(curIP[:-1])
                return
            if dots>4:
                return
            
            # str[i:i+3] but while end of string[i:len(A)]
            for j in range(i,min(i+3,len(A))):
                # leading character in string can not be 0
                if int(A[i:j+1])<256 and (i==j or A[i]!="0"):
                    backtrack(j+1, dots+1 , curIP + A[i:j+1] +".")
        backtrack(0,0,"")
        return res