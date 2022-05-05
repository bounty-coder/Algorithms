# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        k=''
        for i in range(len(s)):
            if (ord(s[i])>=97 and ord(s[i])<=ord('z')) or (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')):
                k+=s[i]
                
        for i in range(len(k)//2):
            if k[i]!=k[len(k)-i-1]:
                return False
        return True

# python approach
def isPalindrome(str):
    return str==str[::-1]