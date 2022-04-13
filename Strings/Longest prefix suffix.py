# Given a string of characters, find the length of the 
# longest proper prefix which is also a proper suffix.

# Input: s = "abab"
# Output: 2

# approach 1 O(s*t)
# def lps(s):
#     for i in range(len(s)-1,0,-1):
#         if s[0:i]==s[len(s)-i:len(s)]:
#             return i
#     return 0

# O(s+t) 
# similar to sliding window
def lps( str):
    A = [0 for i in range(len(str))]
    j = 0;i = 1
    while i < len(str) :
        if str[i] == str[j] :
            A[i] = j+1
            j+=1
            i+=1
        else :
            if j==0 :
                i+=1
            else :
                j = A[j-1]
    return A[-1]

s = "abab"
print(lps(s))