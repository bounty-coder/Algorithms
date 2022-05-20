# Given a positive integer which fits in a 32 bit signed 
# integer, find if it can be expressed as A^P where P > 1
#  and A > 0. A and P both should be integers.

# Algorithm 1
# 1. Initialize factor 2.
# 2. Check if number is divisible by factor".
# If yes, then keep on dividing the number by factor till 
# it is divisible by factor.
# 3. After step 2, if we are left with number = 1, then number can be
# represented as a power of factor, so return true. 
# Else, increment factor by 1
# 4. Repeat steps 2 and 3 till factor <= sqrt(number).
# 5. If no such factor is found, then return false.

def isPower(A):
    z=False  #
    if A==1:
        return True
    for i in range(2,int(A**(0.5))+1):
        x=A 
        while x!=1:
            if x%i==0:
                x=x//i 
            else:
                break
        if x==1:
            z=True
            break
    return z

#Approach 2 optimised fastest
def isPower(self, A):
    for p in range(2,33):
        a=round(A**(1/p))
        if(a**p==A):
            return True 
    return False