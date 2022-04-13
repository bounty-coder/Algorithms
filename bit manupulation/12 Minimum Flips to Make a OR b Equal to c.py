# Given 3 positives numbers a, b and c. Return the minimum flips
# required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).

# Input: a = 2, b = 6, c = 5
# Output: 3

import math

def minFlips( a: int, b: int, c: int) -> int:
    k=int(math.log2(max(a,b,c)))+1
    ans=0
    for i in range(k):
        x,y,z=False,False,False
        if (a&(1<<i)):
            x=True
        if (b&(1<<i)):
            y=True
        if (c&(1<<i)):
            z=True
        
        if x|y != z:
            if z==True:
                ans+=1    
            elif x&y!=True:
                ans+=1    
            else:
                ans+=2           
    return ans

a,b,c=4,2,7
print(minFlips(a,b,c))