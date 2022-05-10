# Given an array A of integers, find the maximum of j - i
# subjected to the constraint of A[i] <= A[j].

# Input 1:  A = [3, 5, 4, 2]
# Output 1:  2

#  Maximum value occurs for pair (3, 4).

# Approach 1 Bruteforce O(n^2)
# Approach 2: using indices and sort the array
def maximumGap(A):
    i=0
    n=len(A)
    if n==1:
        return 0
    res=[]
    for i in range(n):
        res.append([A[i],i])
    res.sort()
    ans=0
    minindex=float("inf")
    for i in range(n):
        minindex=min(minindex,res[i][1])
        ans=max(ans,res[i][1]-minindex)
    return ans

# Approach 3: using suffix array O(n)
# as we sorted the array in prev soln, in this while we look at the array
# we have already one sorted array, the indices one(try to come up with better soln)
def maximumGap(A):
    i=0
    n=len(A)
    if n==1:
        return 0
    suffix=[]
    i=n-1
    temp=A[n-1]
    while i>=0:
        if A[i]>temp:
            temp=A[i]
        suffix.append(temp)
        i-=1
    suffix.reverse()
    
    # applying sliding window approach
    i,j,ans=0,0,0
    while i<n and j<n:
        if A[i]<=suffix[j]:
            ans=max(ans,j-i)
            j+=1
        else:
            i+=1
    return ans