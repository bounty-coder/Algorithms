# Reverse bits of a given 32 bits unsigned integer.

n=int(input())
x=0
i=0
while i<32:
    k=n&1
    x=(x<<1)+k
    n=n>>1
    i+=1
print(x)