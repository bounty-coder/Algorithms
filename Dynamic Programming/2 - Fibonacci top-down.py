n=int(input())
dp=[-1]*(n+1)

def fib(n):
    if n<=1:
        return n
    global dp
    first=0
    second=0
    if dp[n-1]==-1:
        dp[n-1]=fib(n-1)
    else:
        first =dp[n-1]
    if dp[n-2]==-1:
        dp[n-2]=fib(n-2)
    else:
        second=dp[n-2]
    dp[n]= first+second
    return dp[n]

print(fib(n))