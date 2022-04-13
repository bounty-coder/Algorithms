class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(n):
    if n:
        inorder(n.left)
        print(n.data)
        inorder(n.right)

def deleteDeepest(n,change):
    q=[]
    q.append(n)
    while len(q)>0:
        temp=q.pop(0)
        if temp is change:
            temp = None
            return
        if temp.right:
            if temp.right is change:
                temp.right=None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is change:
                temp.left=None
                return
            else:
                q.append(temp.left)

def deletion(n,data):
    if n.left==None and n.right==None:
        if n.data==data:
            return None
        else:
            return n
    key_node=None
    q=[]
    q.append(n)
    temp=None
    while len(q)>0:
        temp=q.pop(0)
        if temp.data==data:
            key_node=temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x=temp.data    #last element
        deleteDeepest(n,temp)
        key_node.data=x
    return n




n=node(10)
n.left=node(11)
n.right=node(12)
n.left.left=node(14)
n.left.right=node(15)
print("Data before deletion:",inorder(n))
deletion(n,11)
print("Data after deletion:", inorder(n))