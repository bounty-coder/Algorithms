# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"

def shortestCommonSupersequence(self, str1, str2):
    m=len(str1)
    n=len(str2)
    t=[[0 for i in range(n+1)] for j in range(m+1)]
    #find the LCS dp table
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif str1[i-1]==str2[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    
    s=""
    i,j=m,n
    #traverse backwards
    while i>0 and j>0:
        if str1[i-1]==str2[j-1]:
            s=str1[i-1]+s
            i-=1
            j-=1
        elif t[i-1][j]>t[i][j-1]:
            s=str1[i-1]+s
            i-=1
        else:
            s=str2[j-1]+s
            j-=1
    #if j!=0 then append str upto j=0
    while j>0:
        s=str2[j-1]+s
        j-=1
    #if i!=0 then append str upto i=0
    while i>0:
        s=str1[i-1]+s
        i-=1
    return s