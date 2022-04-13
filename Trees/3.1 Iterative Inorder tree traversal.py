class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None 

def inorder(root):
    stack=[]
    current=root
    while True:
        # Reach the left most Node of the current Node
        if current is not None:
            stack.append(current)
            current=current.left

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif stack:
            current=stack.pop()
            print(current.data, end=" ")
            current=current.right
        else:
            break
    print()

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

inorder(root)