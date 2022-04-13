# given an array of number. Apply '+' or '-' and given target
# sum must be equal to given target
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3 

# S1+S2=sum(arr)
# S1-S2=target
#=>S1=(sum(arr)-target)/2
# now find the count of subsets with S1 

def findTargetSumWays( arr, target):
    s=(sum(arr)-target)//2
    n=len(arr)
    if (sum(arr)-target)%2==1 or s<0:
        return 0
    if n==1:
        if s==0 and arr[0]==0:
            return 2
        if s==0 or s==arr[0]:
            return 1
        return 0
    t=[[0 for i in range(s+1)]for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(s+1):
            if j==0:
                t[i][j]=1
            elif i==0:
                t[i][j]=0
            else:
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
                else:
                    t[i][j]=t[i-1][j]
    return t[n][s]