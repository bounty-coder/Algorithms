# Given preorder and inorder traversal of a tree, construct the binary tree.

# Input :
#         Preorder : [1, 2, 3]
#         Inorder  : [2, 1, 3]

# Return :
#             1
#            / \
#           2   3

# First element of preorder traversal will be root. Combining this info with inorder traversal.
# tell interviewer about the theory concepts.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:    
    def buildTree(self, A, B):
        if not B:
            return None
        # 1) Pick an element from Preorder. A[0]
        #( the very first element of preorder will be root) 
        # 2) Create a new tree node tNode with the data as the picked element.
        root_pos = B.index(A[0])

        # 3) Find the picked element’s index in Inorder. 
        new_node = TreeNode(A[0])

        # 4) Call buildTree for elements before inIndex and make the
        #  built tree as a left subtree of tNode. 
        new_node.left = self.buildTree(A[1:root_pos+1], B[:root_pos])

        # 5) Call buildTree for elements after inIndex and make the
        #  built tree as a right subtree of tNode. 
        new_node.right = self.buildTree(A[root_pos+1:], B[root_pos+1:])

        # 6) return tNode.
        return new_node