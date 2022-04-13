t=int(input())

while t:
    t-=1
    #w- weight of knapsack
    #no of products
    w,n=map(int,input().split())
    p=[]   # p[0]-> weight of product
            #p[1]-> value of product
    for i in range(n):
        p.append(list(map(int,input().split())))
    
    # why make dp of w and n, cause they are changing
    table = [[-1]*(w+1)]*(n+1)
    
    def knapsack(w,n,p):
        
        if w==0 or n==0:
            return 0
        # if t[n][w]!=-1 then we will change table
        if table[n][w]!=-1:
            return table[n][w]

        # If weight of the nth item is
        # more than Knapsack of capacity W,
        # then this item cannot be included
        # in the optimal solution
        if p[n-1][0]>w:
            table[n][w] = knapsack( w , n-1 , p)
            return table[n][w]

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        elif p[n-1][0]<=w:
            table[n][w] = max(p[n-1][1] + knapsack( w - p[n-1][0] , n-1, p) , knapsack( w , n-1, p))
            return table[n][w]

    print(knapsack(w,n,p))

# @param A : list of value 
# @param B : list of weights
# @param C : integer
# @return an integer
# def solve( A, B, C):
#     n=len(A)
#     t=[[0 for i in range(C+1)]for j in range(n+1)]

#     for i in range(n+1):
#         for j in range(C+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif j<B[i-1]:
#                 t[i][j]=t[i-1][j]
#             else:
#                 t[i][j]=max(t[i-1][j],A[i-1]+t[i-1][j-B[i-1]])
#     return t[n][C]