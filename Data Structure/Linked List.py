class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_beg(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        return

    def insert_vals(self,data):
        self.head=None
        for i in data:
            self.insert(i)

    def ll_len(self):
        if self.head is None:
            return 0
        itr=self.head
        l=0
        while itr:
            itr=itr.next
            l+=1
        return l

    def remove(self,x):
        if x<0 or x>self.ll_len():
            raise Exception("Invalid Index")
        if self.head is None:
            print("Empty List")
            return
        itr=self.head
        if x==0:
            y=self.head
            self.head=self.head.next
            del(y)
            return
        while x-1:
            itr=itr.next
            x-=1
        y=itr.next.next
        del(itr.next)
        itr.next=y    
        return    

    def print(self):
        if self.head is None:
            print("Empty LL")
            return
        itr=self.head
        llstr=' '
        while itr:
            llstr += str(itr.data) + "-->"
            itr=itr.next
        print(llstr)

    

if __name__=='__main__':
    ll=Linkedlist()
    data=['apple','banana','cherry','dragonfruit']
    ll.insert_vals(data)
    ll.insert(3)
    ll.print()
    ll.insert(4)
    ll.insert_beg(10)
    ll.print()
    print("length:",ll.ll_len())
    ll.remove(6)
    ll.print()