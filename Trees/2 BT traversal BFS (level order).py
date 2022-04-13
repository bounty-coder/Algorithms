class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelorder(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    while len(queue):
        print(queue[0].data,end=" ")
        temp=queue.pop(0)
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
            

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

print("level order traversing:",end=" ")
levelorder(root)