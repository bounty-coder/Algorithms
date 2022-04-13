# Given two strings text1 and text2, return the length of their 
# longest common subsequence. If there is no common subsequence, return 0.

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  

def longestCommonSubsequence(X,Y):
        # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
    

str1=input("Enter String 1:")
str2=input("Enter String 2:")
print(longestCommonSubsequence(str1,str2))