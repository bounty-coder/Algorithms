n=int(input())
def fibonacci(n):
    fib=[0]*n
    fib[0]=0
    fib[1]=1
    if n==0:
        return 0
    for i in range(n-2):
        fib[i+2]=fib[i]+fib[i+1]
    return fib


print(fibonacci(n))