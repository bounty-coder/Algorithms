# Given a string you need to print the size of the longest
# possible substring that has exactly K unique characters.
# If there is no possible substring then print -1.

# S = "aabacbebebe", K = 3
# Output: 7
# Explanation: "cbebebe" is the longest 
# substring with K distinct characters.

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        l=0
        i,j=0,0
        dic={}
        
        while j<len(s):
            if s[j] not in dic:
                dic[s[j]]=1
            else:
                dic[s[j]]+=1
                
            if len(dic)<k:
                j+=1
            elif len(dic)==k:
                l=max(l,j-i+1)
                j+=1
            elif len(dic)>k:
                while len(dic)>k:
                    dic[s[i]]-=1
                    if dic[s[i]]==0:
                        del dic[s[i]]
                    i+=1
                j+=1
        if l==0:
            return -1
        else:
            return l
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)
