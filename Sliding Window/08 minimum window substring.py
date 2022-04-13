# Given two strings s and t of lengths m and n respectively,
#  return the minimum window substring of s such that every
#  character in t (including duplicates) is included in the window.
#  If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

def minWindow(s,t):
    m=len(s)
    n=len(t)
    l=float('inf')
    dic={}
    #create map for t
    for i in range(n):
        if t[i] not in dic:
            dic[t[i]]=1
        else:
            dic[t[i]]+=1
    count=len(dic)
    i,j=0,0
    c=""
    #traverse the window
    while j<m:
        # check if exist
        if s[j] in dic:
            dic[s[j]]-=1
            # calculate
            if dic[s[j]]==0:
                count-=1
                
        #condition matching
        while count==0:
            # ans appending
            if l>j-i+1:
                l=j-i+1
                c=s[i:j+1]
                
            # shortning the window from left side
            if s[i] in dic:
                dic[s[i]]+=1
                if dic[s[i]]>0:
                    count+=1
            i+=1
        j+=1
    
    if l>m:
        return ""
    return c

s=input()
t=input()
print(minWindow(s,t))