# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s):
    l=0
    i,j=0,0
    dic=dict()
    k=0
    while j<len(s):
        if s[j] not in dic:
            dic[s[j]]=1
            l=max(l,len(dic))
            j+=1
        else:
            while s[j]!=s[i]:
                del dic[s[i]]
                i+=1
            i+=1
            dic[s[j]]=1
            j+=1
    return l

s=input()
print(lengthOfLongestSubstring(s))