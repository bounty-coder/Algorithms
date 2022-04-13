# Given an integer array arr of size N, the task is to divide it 
# into two sets S1 and S2 such that the absolute difference between
# their sums is minimum and find the minimum difference

# S1+S2=range   S1-S2=diff
# diff=range-2*S1

def minDifference(arr, n):
    # sum of array
    s=sum(arr)
    # dp table
    t=[[0 for i in range(s+1)] for j in range(n+1)]

    # initialising array
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
                
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    
    # initialising a support array to save all those number
    # whose numbers can be formed
    ls=[]
    for j in range(s//2+1):
        if t[n][j]==1:
            ls.append(j)
    
    diff=float("inf")
    for i in range(len(ls)):
        diff=min(diff,s-2*ls[i])
    return diff

arr=list(map(int,input().split()))
n=len(arr)
print(minDifference(arr,n))