# Given an integer x, find the square root of x. If x is
#  not a perfect square, then return floor(√x).
# Input 1: 11
# Output 1: 3

def floorSqrt(self, x): 
    #Your code here
    if x==0 or x==1:
        return x
    i=1
    result=1
    while result<=x:
        i+=1
        result=i*i
    return i-1

x=int(input())
print(floorSqrt(x))
