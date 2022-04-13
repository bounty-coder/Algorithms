# You are given two numbers A and B. The task is to 
# count the number of bits needed to be flipped
#  to convert A to B.

# Input: A = 10, B = 20
# Output: 4
# A  = 01010
# B  = 10100

def countBitsFlip(a,b):
    ##Your code here
    x=a^b
    count=0
    while x:
        x=x&(x-1)
        count+=1
    return count

a = 10
b = 20
print(countBitsFlip(a,b))