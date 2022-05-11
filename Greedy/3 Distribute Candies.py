# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# 1. Each child must have at least one candy.
# 2. Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Input 2: A = [1, 5, 2, 1]
# Output 2:  7
# Candies given = [1, 3, 2, 1]

def candy(A):
    ans=0
    n=len(A)
    left=[1 for i in range(len(A))]
    right=[1 for i in range(len(A))]
    i=1
    while i<n:
        if A[i]>A[i-1]:
            left[i]=left[i-1]+1
        i+=1
    
    j=n-2
    while j>=0:
        if A[j]>A[j+1]:
            right[j]=right[j+1]+1
        j-=1
        
    for i in range(len(A)):
        ans+=max(left[i],right[i])
    return ans

A=list(map(int,input().split()))
print(candy(A))