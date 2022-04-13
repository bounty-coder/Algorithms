# Given an integer array A of size N containing 0's and 1's only. 

# You need to find the length of the longest subarray having count 
# of 1’s one more than count of 0’s.

# Input- A = [0, 1, 1, 0, 0, 1]
# O/p-  5

def solve(A):
    diff=l=0
    n=len(A)
    dic={}
    zero,one=0,0
    for i in range(n):
        if A[i]==0:
            zero+=1
        else:
            one+=1
        diff=one-zero
        if diff==1:
            l=i+1
        if diff-1 in dic:
            l=max(l,i-dic[diff-1])

        if diff not in dic:
            dic[diff]=i
    return l