# find if the array can be partitioned into two subsets such that 
# the sum of elements in both subsets is equal.

# sum of array must be even
#find a subset having sum=sum/2

def canPartition(arr):
    s=sum(arr)
    n=len(arr)
    if s%2==1:
        return False
    else:
        sub=s//2
        t=[[False for i in range(sub+1)] for j in range(n+1)]
        for i in range(n+1):
            t[i][0]=True
        
        for i in range(1,n+1):
            for j in range(1,sub+1):
                if j<arr[i-1]:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=(t[i-1][j] or t[i-1][j-arr[i-1]])
                    
        return t[n][sub]

arr=[1,5,11,5]
print(canPartition(arr))