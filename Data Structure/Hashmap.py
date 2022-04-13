class hashmap:
    def __init__(self):
        self.MAX=1000
        self.arr= [None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h%self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr(h)    

if __name__=='__main__':
    dic=hashmap()
    