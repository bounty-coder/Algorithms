
# Longest Palindromic Substring

# Method 1: Brute Force. 
# The simple approach is to check each substring whether 
# the substring is a palindrome or not. 
# To do this first, run three nested loops, 
# the outer two loops pick all substrings one by one by 
# fixing the corner characters, the inner loop checks 
# whether the picked substring is palindrome or not. 
# Time complexity: O(n^3). 
# Three nested loops are needed to find the longest palindromic 
# substring in this approach, so the time complexity is O(n^3).
# Auxiliary complexity: O(1).

# Method 2: Dynamic Programming. 
# The time complexity can be reduced by storing results of sub-problems.

# Maintain a boolean table[n][n] that is filled in bottom up manner.
# The value of table[i][j] is true, 
# if the substring is palindrome, otherwise false.
# To calculate table[i][j], check the value of table[i+1][j-1],
# if the value is true and str[i] is same as str[j], 
# then we make table[i][j] true.
# Otherwise, the value of table[i][j] is made false.
# We have to fill table previously for substring of length = 1 and length =2 because 
# as we are finding , if table[i+1][j-1] is true or false , so in case of 
# (i) length == 1 , lets say i=2 , j=2 and i+1,j-1 doesn’t lies between [i , j] 
# (ii) length == 2 ,lets say i=2 , j=3 and i+1,j-1 again doesn’t lies between [i , j].

# Time O(n^2) and it requires O(n^2) extra space


import sys

# A utility function to print a
# substring str[low..high]
def printSubStr(st, low, high) :
    sys.stdout.write(st[low : high + 1])
    sys.stdout.flush()
    return ''

# This function prints the longest palindrome
# substring of st[]. It also returns the length
# of the longest palindrome
def longestPalSubstr(st) :
    n = len(st) # get length of input string

    # table[i][j] will be false if substring 
    # str[i..j] is not palindrome. Else 
    # table[i][j] will be true
    table = [[0 for x in range(n)] for y
                          in range(n)] 
    
    # All substrings of length 1 are
    # palindromes
    maxLength = 1
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1
    
    # check for sub-string of length 2.
    start = 0
    i = 0
    while i < n - 1 :
        if (st[i] == st[i + 1]) :
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1
    
    # Check for lengths greater than 2. 
    # k is length of substring
    k = 3
    while k <= n :
        # Fix the starting index
        i = 0
        while i < (n - k + 1) :
            
            # Get the ending index of 
            # substring from starting 
            # index i and length k
            j = i + k - 1
    
            # checking for sub-string from
            # ith index to jth index iff 
            # st[i + 1] to st[(j-1)] is a 
            # palindrome
            if (table[i + 1][j - 1] and 
                      st[i] == st[j]) :
                table[i][j] = True
    
                if (k > maxLength) :
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1
    print("Longest palindrome substring is: ", printSubStr(st, start,
                                               start + maxLength - 1))

    return maxLength # return length of LPS


# Driver program to test above functions
st = "forgeeksskeegfor"
l = longestPalSubstr(st)
print("Length is:", l)

