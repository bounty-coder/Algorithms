# We build a table of n rows (1-indexed). 
# We start by writing 0 in the 1st row. Now in every subsequent row,
#  we look at the previous row and replace each occurrence of 0 with 01,
#  and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in
#  the nth row of a table of n rows.

# 0------------------------------ 2^0
# 0 1---------------------------- 2^1
# 0 1 1 0------------------------ 2^2
# 0 1 1 0 1 0 0 1---------------- 2^3
# |-----|=|-----|
# observation
# 1: n->k  then n+1->k*2
# 2: first half same as (n-1)th and, rest half invert (n-1)th row

def kthGrammar(n,k):
    if n==1 and k==1:
        return 0
    mid = pow(2,n-1)/2
    if k <=mid:
        return kthGrammar(n-1,k)
    else:
        return (kthGrammar(n-1 ,k-mid))^1      #  XOR 0^1=1 and 1^1=0
        
kthGrammar(2,2) #n,k