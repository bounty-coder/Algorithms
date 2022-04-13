# Optimized implementation: 
# The implementation can be optimized by calculating the height in the same
# recursion rather than calling a height() separately. 
# This optimization reduces time complexity to O(n).

# A binary tree Node
class Node:
 
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# utility class to pass height object
 
class Height:
    def __init(self):
        self.h = 0
 
# Optimised recursive function to find diameter
# of binary tree
 
 
def diameterOpt(root, height):
 
    # to store height of left and right subtree
    lh = Height()
    rh = Height()
 
    # base condition- when binary tree is empty
    if root is None:
        height.h = 0
        return 0
 
     
    # ldiameter --> diameter of left subtree
    # rdiamter  --> diameter of right subtree
     
    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter
     
    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)
 
    # height of tree will be max of left subtree
    # height and right subtree height plus1
 
    height.h = max(lh.h, rh.h) + 1
 
    # return maximum of the following
    # 1)left diameter
    # 2)right diameter
    # 3)left height + right height + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
 
# function to calculate diameter of binary tree
def diameter(root):
    height = Height()
    return diameterOpt(root, height)
 
 
# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
"""
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""
 
# Function Call
print(diameter(root))



# GFG answer
class Solution:
    dia=0
    
    #Function to find the diameter of a Binary Tree.
    def util(self,root):
        
        #if node becomes null, we return 0.
        if root == None:
            return 0
        global dia
        
        #calling the util function recursively for the left and 
        #right subtrees to find their heights.
        l=self.util(root.left)
        r=self.util(root.right)
        
        #storing the maximum possible value of l+r+1 in diameter.
        dia=max(dia, l+r+1)
        
        #returning height of subtree.
        return 1 + max(l, r)
    
  
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        global dia
        dia=0
        #calling the function to find the result.
        self.util(root)
        #returning the result.
        return dia

# DFS Solution
def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root: 
                return 0, 0
            left_d, left_h = dfs(root.left)
            right_d, right_h = dfs(root.right)
            return max(left_d, right_d, left_h+right_h), 1+max(left_h, right_h)
 
        return dfs(root)[0]