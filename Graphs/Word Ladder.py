# Given two words, beginWord and endWord, and a dictionary 
# wordList, return the number of words in the shortest 
# transformation sequence from beginWord to endWord, or 0
#  if no such sequence exists.

# Input: beginWord = "hit", endWord = "cog", 
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5

# Explanation: One shortest transformation sequence is
#"hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei=collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
                
        visit=set([beginWord])
        q=collections.deque([beginWord])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    print(pattern)
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res+=1
        return 0