# Given a rod of length N inches and an array of prices, 
# price[] that contains prices of all pieces of size smaller than N.
#  Determine the maximum value obtainable by cutting up the rod and selling the pieces.

# N = 8
# Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
# Output: 22

def cutRod(price, n):
    # initialising the table and values
    t=[[0 for i in range(n+1)] for j in range(n+1)]
    
    # creating the array of 1,2,3,4,...n
    length=[i for i in range(1,n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if length[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=max(price[i-1]+t[i][j-length[i-1]], t[i-1][j])
        # t[i] showing that it is again available for choice
        # if not available for choice then we could have done it t[i-1]
        # like in 0-1 knapsack 

    return t[n][n]

n = int(input())
a = [int(x) for x in input().strip().split()]
print(cutRod(a, n))