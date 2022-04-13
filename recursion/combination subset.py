# Given two integers n and k, return all possible combinations of
#  k numbers out of 1 2 3 ... n.
# Make sure the combinations are sorted.

# If n = 4 and k = 2, a solution is:

# [ [1,2], [1,3], [1,4], [2,3], [2,4],
#   [3,4],]

def combine( A, B):
    p = []
    for i in range(A):
        p.append(i+1)
    
    def combi(A, B):
        l=[]
        if B == 0:
            return []
        if B == 1:
            for i in A:
                l.append([i])
            return l
        else:
            for i in range(len(A)-B+1):
                x = [A[i]]
                xs = A[i+1:]
                for j in combi(xs, B-1):
                    l.append(x + j)
            return l
    
    return combi(p, B)

a,b=map(int,input().split())
print(combine(a,b))