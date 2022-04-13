# Return the number of combinations that make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return 0.

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# similar to count subset of sum k
def change(amount, coins):
        l=len(coins)
        t=[[0 for i in range(amount+1)] for j in range(l+1)]
        for i in range(l+1):
            t[i][0]=1
            
        for i in range(1,l+1):
            for j in range(1,amount+1):
                if coins[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]+t[i][j-coins[i-1]]
        return t[l][amount]

amount = 5
coins = [1,2,5]
print(change(amount,coins))