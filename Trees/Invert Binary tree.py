# Convert a Binary Tree into its Mirror Tree / Invert a BT

# Method 1 (Recursive)

# Algorithm – Mirror(tree): 
 

# (1)  Call Mirror for left-subtree    i.e., Mirror(left-subtree)
# (2)  Call Mirror for right-subtree  i.e., Mirror(right-subtree)
# (3)  Swap left and right subtrees.
#           temp = left-subtree
#           left-subtree = right-subtree
#           right-subtree = temp

 
# Utility function to create a new
# tree node
class newNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
 
""" Change a tree so that the roles of the
    left and right pointers are swapped at
    every node.
"""
def mirror(node):
 
    if (node == None):
        return
    else:
 
        temp = node
         
        """ do the subtrees """
        mirror(node.left)
        mirror(node.right)
 
        """ swap the pointers in this node """
        temp = node.left
        node.left = node.right
        node.right = temp
 
""" Helper function to print Inorder traversal."""
def inOrder(node) :
 
    if (node == None):
        return
         
    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)
 
# Driver code
if __name__ =="__main__":
 
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
 
    """ Print inorder traversal of
        the input tree """
    print("Inorder traversal of the",
               "constructed tree is")
    inOrder(root)
     
    """ Convert tree to its mirror """
    mirror(root)
 
    """ Print inorder traversal of
        the mirror tree """
    print("\nInorder traversal of",
              "the mirror treeis ")
    inOrder(root)

# Worst-case Time complexity is O(n) and for space complexity, 
# If we don’t consider the size of the recursive stack for
# function calls then O(1) otherwise O(h) where h is the height of the tree.