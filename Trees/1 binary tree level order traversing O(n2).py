# Stack method O(n^2)

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelorder(root):
    h=height(root)
    print(h)
    for i in range(1,h+1):
        printcurrent(root,i)

def printcurrent(root,level):
    if root is None:
        return
    if level==1:
        print(root.data,end=" ")
        print("root")
    elif level>1:
        printcurrent(root.left,level-1)
        print("k",end=" ")
        printcurrent(root.right,level-1)
        print("l",end=" ")

def height(root):
    if root is None:
        return 0
    else:
        ldepth=height(root.left)
        rdepth=height(root.right)
        if ldepth>rdepth:
            return ldepth+1
        else:
            return rdepth+1

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.right.right=node(5)

print(levelorder(root))