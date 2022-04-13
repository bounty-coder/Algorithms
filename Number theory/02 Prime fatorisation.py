
# saving all prime factors in list in O(n) using pre computational technique
def O(n):
    prime_fact=[]
    i=2
    while i<=n:
        while n%i==0:
            prime_fact.append(i)
            n/=i

        i+=1

    print(prime_fact)

#TC-sqrt(n)
#for composite numbers, there will be atleast a number below sqrt(n)
# which is a factor of n
def sqrtO(n):
    prime_fact=[]
    i=2
    while i*i<=n:
        while n%i==0:
            prime_fact.append(i)
            n/=i
        i+=1
    # 36=[2,2,3,3]
    # 24=[2,2,2]  3 not included cause it is odd so n's value will be 3 in the end
    # sso checking if n>1 and if yes then include it in the list      
    if n>1:
        prime_fact.append(int(n))
        
    
    print(prime_fact)

n=int(input())
# O(n)
sqrtO(n)