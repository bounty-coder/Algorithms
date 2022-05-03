# Given a matrix, A of size M x N of 0s and 1s. If an element 
# is 0, set its entire row and column to 0.

# Input 1:
#     [   [1, 0, 1],
#         [1, 1, 1], 
#         [1, 1, 1]   ]

# Output 1:
#     [   [0, 0, 0],
#         [1, 0, 1],
#         [1, 0, 1]   ]

def setZeroes(A):
    r=set()
    c=set()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==0:
                r.add(i)
                c.add(j)
    
    for k in r:
        for i in range(len(A[0])):
            A[k][i]=0
    
    for m in c:
        for j in range(len(A)):
            A[j][m]=0
    
    return A

matrix= [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]
print(setZeroes(matrix))