# Input: str1 = "geek",  str2 = "eke"
# Output: 5

# supersequnce= m+n-len(LCS)

#Function to find length of shortest common supersequence of two strings.
def shortestCommonSupersequence(self, X, Y, m, n):
    t=[[0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif X[i-1]==Y[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    
    return m+n-t[m][n]

X,Y=input().split()
print(shortestCommonSupersequence(X,Y,len(X),len(Y)))