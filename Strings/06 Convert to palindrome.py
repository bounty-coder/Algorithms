# Given a string A consisting only of lowercase characters,
# we need to check whether it is possible to make this string
#  a palindrome after removing exactly one character from this.

# If it is possible then return 1 else return 0.

# Input 1:  A = "abcba"
# Output 1: 1
# Input 2: A = "abecbea"
# Output 2: 0

# Approach 1 Bruteforce
# check string for every element remove O(n^2)=
#  O(n) for every element removal and O(n) inside to check 
# if it's  palindrome

# Approach 2- 2 pointer method
#We start looping in the string by keeping two pointers at both
#  the ends which traverse towards mid position after each iteration,
#  this iteration will stop when we find a mismatch, as it is 
# allowed to remove just one character we have two choices here 
# so we remove both characters one by one and check that after 
# removing that character still string is palindrome or not

class Solution:
    # @param A : string
    # @return an integer

    def isPalindrome(self, s):
        return s == s[::-1]

    def solve(self, A):
        n = len(A)
        start = 0
        end = n - 1
        while start <= end:
            if A[start] != A[end]:
                if self.isPalindrome(A[start + 1:end + 1]) or self.isPalindrome(A[start:end]):
                    return 1
                else:
                    return 0
            start += 1
            end -= 1
        
        return 1