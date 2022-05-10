# Given numRows, generate the first numRows of Pascal's triangle.
# Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

# Example:

# Given numRows = 5,

# Return

# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

def solve(A):
    t1=[1]
    t2=[1,1]
    if A==0:
        return []
    elif A==1:
        return [t1]
    elif A==2:
        return [t1, t2]
    ans=[t1,t2]
    for i in range(3,A+1):
        temp=ans[-1]
        r=[temp[0]]
        i=0
        while i<(len(temp)-1):
            r.append(temp[i]+temp[i+1])
            i+=1
        r.append(temp[i])
        ans.append(r)
    return ans