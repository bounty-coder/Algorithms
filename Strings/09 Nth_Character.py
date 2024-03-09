# Given a binary string s. Perform r iterations on string s, where in each iteration 0 becomes 01 and 1 becomes 10.
# Find the nth character (considering 0 based indexing) of the string after performing these r iterations

# Input:
# s = "1100"
# r = 2
# n = 3
# Output: 1
# Explanation: 
# After 1st iteration s becomes "10100101".
# After 2nd iteration s becomes "1001100101100110".
# Now, we can clearly see that the character at 3rd index is 1, and so the output.

#naive approach
def nthCharacter(s, r, n):
    # code here
    for i in range(r):
        x=""
        for j in range(len(s)-1):
            if s[j]=="0":
                x+="01"
            else:
                x+="10"
        s=x
    if len(s)<=n:
        return 0
    return s[n]


#Efficient approach
def nthCharacter(s, r, n):
      a=n//(2**r)
      rem=n%(2**r)
      b=s[a]
      for i in range(r):
          x=""
          for j in range(len(b)):
              if b[j]=="0":
                  x+="01"
              else:
                  x+="10"
          b=x
      return b[rem]
