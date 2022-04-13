def isPowerOfFour(n):
    if n==1:
        return True
    if n<4:
        return False
    while n:
        if n&11!=0 and n>>2!=0:
            return False
        n=n>>2
    return True

def isPowerOfThree(n):
    if n<1:
        return False
    if n==1:
        return True
    while n>1:
        if n%3!=0:
            return False
        n/=3
    if n==1:
        return True
    return False

def isPowerOfTwo(n):
    if n==0:
        return False
    while n:
        if n&1==1 and n>>1!=0:
            return False
        n=n>>1
    return True

n=int(input())
print(isPowerOfTwo(n),isPowerOfThree(n),isPowerOfFour(n))