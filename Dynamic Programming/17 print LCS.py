def LCS(str1, str2):
        
    m=len(str1)
    n=len(str2)
    t=[[None for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif str1[i-1]==str2[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    print(i,j)
    seq=""
    i,j=m,n
    print()
    while i>0 and j>0:
        print(str1[i-1]+" "+ str2[j-1])
        if str1[i-1]==str2[j-1]:
            seq+=str1[i-1]
            i-=1
            j-=1
            
        elif str1[i-1][j]>str2[i][j-1]:
            i-=1
        else:
            j-=1
    return reversed(seq)


str1=input("Enter string1:")
str2=input("Enter string2:")
print(LCS(str1,str2))