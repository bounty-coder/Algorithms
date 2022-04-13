# Given a string, print the longest repeating subsequence such
#  that the two subsequence don’t have same string character at same position

# input- str="AABEBCDD"
# op- "ABD"

# copy the string and find LCS but,
# keep in mind that index of element must not be matched
# i!=j rest is same as LCS

def LongestRepeatingSubsequence(self, s):
    # Code here
    m=len(s)
    t=[[0 for i in range(m+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j]=0
            elif s[i-1]==s[j-1] and i!=j:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[m][m]

str = input()
ans = LongestRepeatingSubsequence(str)
print(ans)