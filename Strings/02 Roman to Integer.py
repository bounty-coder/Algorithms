# Given a string A representing a roman numeral.
# Convert A into integer.
# A is guaranteed to be within the range from 1 to 3999.

# Input 1:  A = "XIV"
# Output 1:  14

# Split the Roman Numeral string into Roman Symbols (character).
# Convert each symbol of Roman Numerals into the value it represents.
# Take symbol one by one from starting from index 0: 
# If current value of symbol is greater than or equal to the value of 
# next symbol, then add this value to the running total.
# else subtract this value by adding the value of next symbol 
# to the running total.

class Solution:
    # @param A : string
	# @return an integer
    def romanToInt(self, A):
        def sym(x):
            if x=="M":
                return 1000
            elif x=="D":
                return 500
            elif x=="C":
                return 100
            elif x=="L":
                return 50
            elif x=="X":
                return 10
            elif x=="V":
                return 5
            elif x=="I":
                return 1
            return -1
        res=0
        i=0

        while i<len(A):
            s1=sym(A[i])
            if i+1<len(A):
                s2=sym(A[i+1])
                if s1>=s2:
                    # Value of current symbol is greater
                    # or equal to the next symbol
                    res=res+s1
                    i+=1
                else:

                    res=res+s2-s1
                    i+=2
            else:
                res=res+s1
                i+=1
        return res