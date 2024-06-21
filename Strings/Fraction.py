'''
You are given a string str containing two fractions a/b and c/d, compare them and return the greater. If they are equal, then return "equal".

Note: The string str contains "a/b, c/d"(fractions are separated by comma(,) & space( )). 
'''

'''
Input: str = "5/6, 11/45"
Output: 5/6
Explanation: 5/6=0.8333 and 11/45=0.2444, So 5/6 is greater fraction.
'''

# Method 1 : Parsing
#User function Template for python3


class Solution:
    def compareFrac (s):
        a,b=s.split(", ")
        a1,a2 = map(int,a.split("/"))
        b1,b2 = map(int,b.split("/"))
        one=a1/a2
        two=b1/b2
        if one>two:
            return "%d/%d" % (a1,a2)
        elif one<two:
            return "%d/%d" % (b1,b2)
        return "equal"



#Method 2: using fractions

from fractions import Fraction

def compareFrac (s):
    a,b=s.split(", ")
    a1,a2 = map(int,a.split("/"))
    b1,b2 = map(int,b.split("/"))
    one=Fraction(a)
    two=Fraction(b)
    if one>two:
        return a
    elif one<two:
        return b
    return "equal"
