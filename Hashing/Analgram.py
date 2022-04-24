# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic=dict()
        for i in range(len(s)):
            if s[i] in dic.keys():
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
                
        for i in range(len(t)):
            if t[i] in dic.keys():
                dic[t[i]]-=1
                if dic[t[i]]<0:
                    return False
            else:
                dic[t[i]]=-1
        
        for i in dic.values():
            if i!=0:
                print(i)
                return False
            
        return True