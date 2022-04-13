class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if (not root):
        return
    
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def insertnode(root,n):
    if not root:
        root=node(n)
        return
    q=[]
    q.append(root)
    while len(q):
        temp=q.pop(0)
        if temp.left is not None:
            q.append(temp.left)
        else:
            temp.left=node(n)
            break
        if temp.right is not None:
            q.append(temp.right)
        else:
            temp.right=node(n)
            break

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.right.right=node(5)

inorder(root)
n=input("Enter a number:")
insertnode(root,n)
m=input("Enter a number:")
insertnode(root,m)
m=input("Enter a number:")
insertnode(root,m)
inorder(root)