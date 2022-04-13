# Longest Palindromic Substring 2

# The idea is to generate all even length and 
# odd length palindromes and keep track of the 
# longest palindrome seen so far.
# To generate odd length palindrome, Fix a center 
# and expand in both directions for longer palindromes,
# i.e. fix i (index) as the center and
# two indices as i1 = i+1 and i2 = i-1
# Compare i1 and i2 if equal then decrease i2 and
#  increase i1 and find the maximum length. 
# Use a similar technique to find the even-length palindrome.
# Take two indices i1 = i and i2 = i-1 and 
# compare characters at i1 and i2 and 
# find the maximum length till all pairs of 
# compared characters are equal and store the maximum length.
# Print the maximum length.

# A O(n ^ 2) time and O(1) space program to find the
# longest palindromic substring
 
# This function prints the longest palindrome substring (LPS)
# of str[]. It also returns the length of the longest palindrome
 
 
def longestPalSubstr(string):
    maxLength = 1
 
    start = 0
    length = len(string)
 
    low = 0
    high = 0
 
    # One by one consider every character as center point of
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1
 
        # Move back to the last possible valid palindrom substring
        # as that will anyway be the longest from above loop
        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
          start = low
          maxLength = high - low + 1
 
        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1
 
        # Move back to the last possible valid palindrom substring
        # as that will anyway be the longest from above loop
        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
          start = low
          maxLength = high - low + 1
 
    print ("Longest palindrome substring is:",end=" ")
    print (string[start:start + maxLength])
 
    return maxLength
 
 
# Driver program to test above functions
string = ("forgeeksskeegfor")
print ("Length is: " + str(longestPalSubstr(string)))