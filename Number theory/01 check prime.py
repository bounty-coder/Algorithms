n=int(input())
is_prime=True
if n==1:
    is_prime=False
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break
print(is_prime)