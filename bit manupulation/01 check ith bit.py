# Given a number N and a bit number K, check if Kth bit of N is
# set or not. A bit is called set if it is 1. Position of set bit
#  '1' should be indexed starting with 0 from LSB side in
# binary representation of the number.
# Input: N = 4, K = 0
# Output: No
import math

    #Function to check if Kth bit is set or not.
def checkKthBit(n, k):
    return ((1<<k)&n);
        
n=int(input())
k=int(input())
if checkKthBit(n,k):
    print("Yes")
else:
    print("No")