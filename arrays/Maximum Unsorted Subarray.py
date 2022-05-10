# Given an array A of non-negative integers of size N. 
# Find the minimum sub-array Al, Al+1 ,..., Ar such that if
# we sort(in ascending order) that sub-array, then the whole array
#  should get sorted.If A is already sorted, output -1.

# A = [1, 3, 2, 4, 5]
# op- [1, 2]

def subUnsort(A):
    n=len(A)
    s,e=-1,-1
    i=0
    while i<n-1:
        if A[i]>A[i+1]:
            s=i
            break
        i+=1
        
    if s==-1:
        return [-1]
    
    j=n-1
    while j>0:
        if A[j]<A[j-1]:
            e=j
            break
        j-=1
    
    minval,maxval=float("inf"),float("-inf")
    for i in range(s,e+1):
        minval=min(minval,A[i])
        maxval=max(maxval,A[i])
    
    for i in range(0,s+1):
        if A[i]>minval:
            s=i
            break

    for i in range(n-1,e,-1):
        if A[i]<maxval:
            e=i 
            break
    return [s,e]

A=list(map(int,input().split()))
print(subUnsort(A))