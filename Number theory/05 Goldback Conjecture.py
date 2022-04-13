#User function Template for python3

def getPrimes(N):
    if N<=2 :
        return [-1,-1]
    
    isprime=[True for i in range(N)]
    isprime[0]=isprime[1]=False
    for i in range(2,N):
        if isprime[i]==True:
            j=2*i           # more optimise j=i*i
            
            while j<N:
                isprime[j]=False
                j+=i
    
    for i in range(2,N//2+1):
        if isprime[i]==True and isprime[N-i]==True:
            return [i,N-i]
    
    return [-1,-1]
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3


N=int(input())

ptr = getPrimes(N)

print(ptr[0],ptr[1])
