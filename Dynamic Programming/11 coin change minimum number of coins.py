# Return the fewest number of coins that you need to make up 
# that amount. If that amount of money cannot be made up by 
# any combination of the coins, return -1.


def coinChange(coins,amount):
    l=len(coins)
    
    #initialising table with +inf
    t=[[float("inf") for i in range(amount+1)]for j in range(l+1)]
    #at amount=0, l=0
    for i in range(1,l+1):
        t[i][0]=0
    
    # unbounded knapsack
    for i in range(1,l+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                t[i][j]=min(t[i][j-coins[i-1]]+1,t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
                
    if t[l][amount]==float("inf"):
        return -1
    return t[l][amount]

coins=list(map(int,input().split()))
amount=int(input())
print(coinChange(coins,amount))


# better solution

# def coinChange(coins, amount):
#     # Max Value stored as amount+1
#     dp = [amount+1] * (amount+1)
#     dp[0] = 0
#     for i in range(1, amount+1):
#         for c in coins:
#             if 0 <= i-c:
#                 dp[i] = min(dp[i],1+dp[i-c])
#     return dp[amount] if dp[amount] != amount+1 else -1