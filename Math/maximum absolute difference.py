# You are given an array of N integers, A1, A2 ,…, AN. Return
# maximum value of f(i, j) for all 1 ≤ i, j ≤ N.

# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# For example, # A=[1, 3, -1]

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

# |x| => +x or -x
# |A[i] - A[j]| => A[i]-A[j] or -A[i]+A[j]
#  |i - j| => i-j or -i+j
# so total 4 combinations
# 1. A[i]-A[j]+i-j => (A[i]+i)-(A[j]+j)
# 2. A[i]-A[j]-i+j => (A[i]-i)-(A[j]-j)
# 3. -A[i]+A[j]+i-j => -(A[i]-i)+(A[j]-j)
# 4. -A[i]+A[j]-i+j => -(A[i]+i)+(A[j]+j)
# here 1 and 4 are equal and 2 and 3 are equal
def maxArr(A):
    if len(A)==0:
        return 0
    max1,min1,max2,min2=float("-inf"),float("inf"),float("-inf"),float("inf")
    for i in range(len(A)):    
        max1=max(max1,A[i]+i)     
        max2=max(max2,-A[i]+i)
        
        min1=min(min1,A[i]+i)
        min2=min(min2,-A[i]+i)
    # print(max1,min1,max2,min2)
    ans=max(max1-min1,max2-min2)
    return ans

A=list(map(int(input().split())))
print(maxArr(A))