class node:
    def __init__(self,data=None,nxt=None):
        self.data=data
        self.nxt=nxt

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        n=node(data,self.head)
        self.head=n

    def append(self,data):
        if self.head is None:
            self.head=node(data,None)
            return
        temp=self.head
        while temp.nxt:
            temp=temp.nxt
        temp.nxt=node(data,None)
        return
    
    def insert_array(self,data):
        self.head=None
        for i in data:
            self.append(i)

    def printlist(self):
        if self.head is None:
            return 0
        temp=self.head
        while temp:
            print(temp.data,'->',end=' ')
            temp=temp.nxt
        print(' ')


l=LinkedList()
l.push(1)
l.push(2)
l.printlist()
a=LinkedList()
a.append(5)
a.append(6)
a.printlist()
arr=[11,12,13,14]
n=LinkedList()
n.insert_array(arr)
n.printlist()
brr=[16,17,18,19]
n.insert_array(brr)
n.printlist()