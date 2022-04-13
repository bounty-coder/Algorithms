# Find All Anagrams in a String
# Given two strings s and p, return an array of all 
# the start indices of p's anagrams in s. 

# An Anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def findAnagrams(s,p):
    n=len(s)
    k=len(p)
    # hashmap to store the all distinct keys of p
    dic={}
    for i in p:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    i,j=0,0
    ls=[]
    # distinct elements in dictionary-->cnt
    cnt=len(dic)

    while j<n:
        # j matches in dic, s[j] will be decreased
        if s[j] in dic:
            dic[s[j]]-=1
            #any element decreased to 0, 
            if dic[s[j]]==0:
                cnt-=1
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            if cnt==0:
                ls.append(i)
                
            
            if s[i] in dic:
                dic[s[i]]+=1
                #any element increased from 0,check
                if dic[s[i]]==1:
                    cnt+=1
            i+=1
            j+=1
    return ls

s = "forxxorfxdofr"
p = "for"
print(findAnagrams(s,p))