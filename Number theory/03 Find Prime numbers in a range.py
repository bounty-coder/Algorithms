# Given two integers M and N, generate all primes between M and N.
# Input:  M=1,N=10
# Output:  2 3 5 7

#User function Template for python3

 
def isprime(k):
    prime=True
    if k==1:
        prime=False
    else:
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                prime=False
                break
    return prime
    
def primeRange(M,N):
    primerange=[]
    i=M
    while i<=N:
        if isprime(i):
            primerange.append(i)
        i+=1
    return primerange

import math
M,N=map(int,input().strip().split(" "))
print(primeRange(M,N))