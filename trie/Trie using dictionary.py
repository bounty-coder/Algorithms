# Trie is a efficient information reTrieval data structure 

# Search is optimal and efficient in Trie

# dictionary searching takes O(1) time complexity but
#  space complexity is O(number of words)

# using trie space complexity will reduce to 


class Trie:
    head={}

    #time complexity O(key_length)
    def add(self,word):
        cur=self.head

        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]

        cur['*']=True


    #time complexity O(key_length)
    def search(self, word):
        cur= self.head
        for i in word:
            print(i,end="")
            if i not in cur:
                print(repr(cur))
                return False
            cur=cur[i]
        if '*' in cur:
            print(repr(cur))
            return True
        else:
            return False

## Instead of returning true or false, 
# can you make it return all the entries in the dictionary starting with the characters you have entered?
#  So it will work like autocomplete suggestions

dic=Trie()
dic.add("aman")
dic.add("amanaa")
print(dic.search("amit"))
print(dic.search("aman"))