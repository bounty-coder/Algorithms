# Given a String, find the longest palindromic subsequence.

# S = "bbabcbcab"
# Output: 7

# longest palindromic subseq will be get through LCS of given
# string and reverse of given string 
def longestPalinSubseq(self, S):
    R=S[::-1]
    m=len(S)
    t=[[0 for i in range(m+1)]for j in range(m+1)]
    
    for i in range(m+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j]=0
            elif S[i-1]==R[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[m][m]

s = input()
ans = longestPalinSubseq(s)
print(ans)