# Given an integer n, return an array ans of length n + 1 such
#  that for each i (0 <= i <= n), ans[i] is the number of 1's
#  in the binary representation of i.

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# O(n) using dp
def countBits( n):
    t=[0 for i in range(n+1)]
    if n==0:
        return t
    t[0]=0
    t[1]=1
    for i in range(2,n+1):
        t[i]=(i&1)+t[i>>1]
    return t

# O(nlogn)
def countBits( n):
    t=[0 for i in range(n+1)]
    for i in range(n+1):
        count=0
        k=i
        while k:
            count+=1
            k=k&(k-1)
        t.append(count)
    return t