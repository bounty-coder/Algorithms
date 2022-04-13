# Given two strings. The task is to find the length 
# of the longest common substring.

# Input: S1 = "ABCDGH", S2 = "ACDGHR"
# Output: 4

def longestCommonSubstr(S1, S2, n, m):
    #initialising table
    t=[[None for i in range(n+1)]for j in range(m+1)]

    ans=0

    # t[m+1][n+1] in bottom up fashion
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            
            elif S2[i-1]==S1[j-1]:
                t[i][j]=t[i-1][j-1]+1
                ans=max(t[i][j],ans)
            
            else:
                t[i][j]=0
    return ans

str1=input("Enter String 1:")
str2=input("Enter String 2:")
print(longestCommonSubstr(str1,str2))