# find a subsequence of array in which the subsequence’s elements
#  are in strictly increasing order, and in which the subsequence
#  is as long as possible. 

# Input 1:
#     A = [1, 2, 1, 5]

# Output 1:
#     3

def lis( A):
    n=len(A)
    t=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if A[i]>A[j] and t[i]<t[j]+1:
                t[i]=t[j]+1
    maximum=0
    for i in range(n):
        maximum=max(maximum,t[i])
    return maximum