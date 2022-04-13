class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        newnode=node(data,self.head)
        self.head=newnode
    
    def printlist(self):
        if self.head is None:
            print("Empty")
            return
        itr=self.head
        llstr=''
        while itr!=None:
            llstr+=str(itr.data)+'->'
            itr=itr.next
        print(llstr)
    
    def count_ele(self):
        if self.head is None:
            return 0
        itr=self.head
        ptr=self.head
        n=0
        while ptr!=None and ptr.next!=None:
            n+=1
            itr=itr.next
            ptr=ptr.next.next
        print(itr.data)

ll=linkedlist()
for i in range(5):
    ll.push(input())
ll.printlist()
ll.count_ele()