# DFS (Depth-first search) is technique used for traversing tree or
#  graph. Here backtracking is used for traversal. In this traversal
#  first the deepest node is visited and then backtracks to it’s 
# parent node if no sibling of that node exist.

# In graph, there might be cycles and dis-connectivity. Unlike graph,
# tree does not contain cycle and always connected.


class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


# Algorithm Preorder(tree)
#    1. Visit the root.
#    2. Traverse the left subtree, i.e., call Preorder(left-subtree)
#    3. Traverse the right subtree, i.e., call Preorder(right-subtree)
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
   
    # for return in list
    # if (root is None):
    #     return []
    # else:
    #     return [root.data]+preorder(root.left)+preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")


root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

print("Preorder:",preorder(root))
print("Postorder:",postorder(root))
print("Inorder:",inorder(root))