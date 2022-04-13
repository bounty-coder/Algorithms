# array- TC O(n/2)
# LL- define a midpointer at size/2+1 but if pushed an element
#   then we can't move mid back and assign it as LL back move can't happen
# Double LL- yes it moves both side so this DS is best for mid O(1)

# Change mid pointer in two cases
# 1) Linked List is empty
# 2) Number of nodes in linked list is odd 

class Node:
    def __init__(self,val):
        self.prev=None
        self.val=val
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.mid=None
        self.count=0

    def push(self,val):
        newnode=Node(val)
        ''' Since we are adding at the beginning,prev is always NULL '''
        newnode.next=s.head
        ''' link the old list off the new DLLNode '''
        newnode.prev=None
        ''' Increment count of items in stack '''
        s.count+=1

        if s.count==1:
            s.mid=Node
        else:
            s.head.prev=newnode
            # Update mid if s->count is odd
            if s.count%2!=0:
                s.mid=s.mid.prev
        # move head to point to the new DLLNode
        s.head=newnode

    def pop(self):
        if s.count==0:
            print("Empty!!")
            return -1
        head=s.head
        item=head.val
        s.head=head.next

        # If linked list doesn't become empty,
        # update prev of new head as NULL
        if s.head!=None:
            s.head.prev=None
        s.count-=1
        
        # update the mid pointer when
        # we have even number of elements
        # in the stack, i,e move down
        # the mid pointer
        if s.count%2==0:
            s.mid=s.mid.next
        return item

    def findmid(self):
        if s.count==0:
            print("Stack is empty")
            return -1
        return s.mid.val

def createStack():
    s=Stack()
    s.count=0
    return s

s=createStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("Middle Element is " +str(s.findmid()))
print("Item popped is " + str(s.pop()))
print("Middle Element is " +str(s.findmid()))