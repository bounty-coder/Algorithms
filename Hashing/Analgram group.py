# Given an array of strings, return all groups of strings that are anagrams.
# Represent a group by a list of integers 
# representing the index in the original list.

# Input : cat dog god tca
# Output : [[1, 4], [2, 3]]


# idea is to sort each strings, then the strings which are 
# anagrams are equal. After that, we can simply group them together 
class Solution:
    # @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
		dic={}
		for i in range(len(A)):
            #sorted will create a list of sorted alphabets
			k="".join(sorted(A[i]))
			if k in dic:
				dic[k].append(i+1)
			else:
				dic[k]=[i+1]
		res=[]
		
		for i in dic:
			res.append(dic[i])
		return res