# Given an array arr[] of N non-negative integers representing the height of blocks.
# If width of each block is 1, compute how much water can be trapped between the blocks
#  during the rainy season. 

def trappingWater(arr,n):
    #Code here
    l=[0]*n
    r=[0]*n
    m=0
    for i in range(n):
        m=max(m,arr[i])
        l[i]=m
    m=0
    for i in range(n-1,-1,-1):
        m=max(m,arr[i])
        r[i]=m
    print(l,r)
    i=0
    s=0
    m=min(arr[0],arr[n-1])
    while i<n:
        s+=min(l[i],r[i])-arr[i]
        i+=1
    return s
            
#{ 
#  Driver Code Starts

import math

arr=[int(x) for x in input().strip().split()]
n=len(arr)
print(trappingWater(arr,n))

# } Driver Code Ends