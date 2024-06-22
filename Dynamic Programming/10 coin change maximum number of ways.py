# Return the number of combinations that make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return 0.

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1


# recursive solution
def count(self, coins, n, Sum):
    count=0
    def rec(n,s,count):
        if n<1 or s>Sum:
            return 0
        if s==Sum:
            count+=1
            return count
        
        include=rec(n,s+coins[n-1],count)
        exclude=rec(n-1,s,count)
        return include+exclude
    s=0
    count=rec(n,s,count)
    return count


# now let's make this recursive code to memoised by adding a cache table in it
def count(self, coins, n, Sum):
    # count=0
    dp=[[0 for i in range(n+1)]for j in range(Sum+1)]
    def rec(n,s):
        if n==0 or s>Sum:
            # dp[s][n]=0
            return 0#dp[s][n]
        if s==Sum:
            dp[s][n]=1
            return dp[s][n]
        if dp[s][n]!=0:
            return dp[s][n]
        include=rec(n,s+coins[n-1])
        exclude=rec(n-1,s)
        dp[s][n]=include+exclude
        return dp[s][n]
    
    s=0
    count=rec(n,s)
    return count



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
