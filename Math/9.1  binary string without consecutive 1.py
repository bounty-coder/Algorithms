# https://practice.geeksforgeeks.org/contest/gfg-weekly-163-rated-contest/problems

# You are given two integers (X) and (Y). You have to count the number of binary strings which have (X) 1’s and (Y) 0’s, and there are no two consecutive 1’s in the string.
# Note: The answer can be too large, so return it with modulo (10^9 + 7)

# The problem can be solved using combinatorial mathematics, 
# consider the problem as placing X 1's into Y + 1 gaps created by Y 0's, and use combinations to count the valid arrangements.
# We will have to calculate (Y+1)CX.

class Solution:
    def CountString(self,X,Y):
        mod = 10**9+7
        def ncr(n,r):
            r = min(r,n-r)
            nr = 1
            dr = 1
            for i in range(r):
                nr  = (nr*(n-i))%mod
                dr = (dr*(i+1))%mod
            
            return (nr*pow(dr,mod-2,mod))%mod
        
        if X>Y+1:
            return 0
        return ncr(Y+1,X) 
