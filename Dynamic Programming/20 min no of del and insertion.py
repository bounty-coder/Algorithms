# str1 = "heap", str2 = "pea" 
# Output : 3
# Minimum Deletion = 2    #len(str1-lcs)
# Minimum Insertion = 1   #len(str2-lcs)
def minOperations(s1, s2):
    m=len(s1)
    n=len(s2)
    t=[[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif s1[i-1]==s2[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])

    delete=m-t[m][n]
    insert=n-t[m][n]

    return delete+insert

s1,s2 = input().split()
ans = minOperations(s1,s2)
print(ans)