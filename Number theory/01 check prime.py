n=int(input())
is_prime=True
if n<=1:
    is_prime=False
elif n==2:
    is_prime=True
elif n%2==0:
    is_prime=False
else:
    for i in range(3, int(n**(1/2))+1, 2):
        if n%i==0:
            is_prime=False
            break
print(is_prime)