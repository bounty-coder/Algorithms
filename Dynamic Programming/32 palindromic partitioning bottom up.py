# Given a string str, a partitioning of the string is a palindrome
# partitioning if every sub-string of the partition is a palindrome.
# Determine the fewest cuts needed for palindrome partitioning of given string.

# Input: str = "ababbbabbababa"
# Output: 3
# Explaination: After 3 partitioning substrings 
# are "a", "babbbab", "b", "ababa".

#variation of MCM
# Soln
# take i=0 and j=n-1 and keep traversing k from i to j 
# and cut the str 
class Solution:
    t=[[-1 for i in range(600)]for j in range(600)]
    
    def ispalindrome(self,s,i,j):
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
        
    def solve(self,s,i,j):
        if i>=j:
            return 0
        if self.ispalindrome(s,i,j):
            return 0

        if self.t[i][j]!=-1:
            return self.t[i][j]
        
        ans=float("inf")
        for k in range(i,j):
            if self.t[i][k]!=-1:
                left=self.t[i][k]
            else:
                left=self.solve(s,i,k)
                self.t[i][k]=left
            
            if self.t[k+1][j]!=-1:
                right=self.t[k+1][j]
            else:
                right=self.solve(s,k+1,j)
                self.t[k+1][j]=right    
            ans=min(1+left+right,ans)
        self.t[i][j]=ans
        return self.t[i][j]
        
        
    def palindromicPartition(self, string):
        # code here
        n=len(string)
        i,j=0,n-1
        return self.solve(string,i,j)

if __name__ == '__main__':
    string = input()
    ob = Solution()
    print(ob.palindromicPartition(string))

# This problem is a variation of Matrix Chain Multiplication problem. 
# If the string is a palindrome, then we simply return 0. Else, 
# like the Matrix Chain Multiplication problem, we try making cuts 
# at all possible places, recursively calculate the cost for each
# cut and return the minimum value. 