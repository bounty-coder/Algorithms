# Given an integer n, generate a square matrix filled with 
# elements from 1 to n2 in spiral order.

# Input 2:  4

# Output 2:
#     [   [1, 2, 3, 4],
#         [12, 13, 14, 5],
#         [11, 16, 15, 6],
#         [10, 9, 8, 7]   ]

def generateMatrix( n):
    matrix=[[0 for i in range(n)]for j in range(n)]
    t,b,l,r=0,n-1,0,n-1
    d=0
    k=1
    while t<=b and l<=r:
        if d==0:
            for i in range(l,r+1):
                matrix[t][i]=k
                k+=1
            t+=1
        elif d==1:
            for i in range(t,b+1):
                matrix[i][r]=k 
                k+=1
            r-=1
        elif d==2:
            for i in range(r,l-1,-1):
                matrix[b][i]=k 
                k+=1
            b-=1
        elif d==3:
            for i in range(b,t-1,-1):
                matrix[i][l]=k
                k+=1
            l+=1
        d=(d+1)%4
    return matrix

