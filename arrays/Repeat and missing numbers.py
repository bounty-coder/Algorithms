# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except X which appears 
# twice and Y which is missing.

# Return X and Y.

# approach
#1- use bruteforce
#2- use sorting
#3- hashmap
#4- count array

#5 two equations- 
# S= n(n+1)/2 - X +Y
# P= 1*2...*n * Y /X
def repeatedNumber( A):
    n=len(A)

    #sum of first natural n numbers
    sum_n = (n*(n+1))//2 
    # sum, product of given array
    arr_sum,arr_prod=0,1
    # product of n natural numbers
    prod_n=1
    for i in range(1,n+1):
        arr_prod*=A[i-1]
        arr_sum+=A[i-1]
        prod_n*=i

    y= int((sum_n-arr_sum)*arr_prod)/(prod_n-arr_prod))
    x=y+sum_n-arr_sum

    return y,x

# 6 
def repeatedNumber(A):
    n = len(A)
    x = sum(A) - sum(set(A))
    k = sum(A) - int(n*(n+1)/2)

    return [x,x-k] 