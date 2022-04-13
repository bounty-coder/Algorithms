
class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False
        self.cntEndWith=0
        self.cntPrefix=0

class Trie:
    # Trie data structure class
    
    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self,ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch)-ord('a')

    def insert(self,key):
        
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

        pCrawl.cntEndWith+=1

    def search(self, key):
        
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord

    def countWordsEqualTo(self, key):
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])
            if pCrawl.children[index]:
                pCrawl=pCrawl.children[index]
            else:
                return 0
        return pCrawl.cntEndWith
    
    def countWordsStartingWith(self,key):
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])
            if pCrawl.children[index]:
                pCrawl=pCrawl.children[index]
            else:
                return 0
        return pCrawl.cntPrefix

    def erase(self,key):
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])
            if pCrawl.children[index]:
                pCrawl=pCrawl.children[index]
                pCrawl.cntPrefix-=1
            else:
                return
        pCrawl.cntEndWith-=1
                