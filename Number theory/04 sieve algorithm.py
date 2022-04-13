

N=10**7
# precompute prime numbers
# first mark all numbers as prime
isprime=[True for i in range(0,N)]
#exceptions
isprime[0]=isprime[1]=False
# start from 2 and mark down all the multiples as nonprime(false)
# any number coming as not marked will be surely be prime 
for i in range(2,N):
    if isprime[i]==True:
        j=2*i           # more optimise j=i*i
        while j<N:
            isprime[j]=False
            j+=i
#TC- n/2 + n/3 + n/4 +.....=nlogn
# but here we have no non-primes
# n/2 + n/3 + n/5 + n/7+.....= n(log(log n))

q=int(input())
print(isprime[q])