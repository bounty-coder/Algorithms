# Given an array, find number of subsets S1 and S2 with a given difference

# arr=[1,1,2,3]
# diff= 1
# o/p-> 2

# S1+S2=sum(arr)
# S1-S2=diff
#=>S1=(sum(arr)+diff)/2
# now find the count of subsets with S1 

def countSubset(arr,diff):
    s=(sum(arr)+diff)//2
    n=len(arr)
    t=[[0 for i in range(s+1)] for j in range(n+1)]
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


arr=[1,1,2,3]
diff=1

print(countSubset(arr,diff))