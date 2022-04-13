# Given inorder and postorder traversal of a tree, construct the binary tree.

# Input : 
#         Inorder : [4, 2, 1, 3, 5 ]
#         Postorder : [4, 2, 5, 3, 1]

# # O/P:  1
#       2   3 
#     4       5

class TreeNode:
    	def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
# 1. We first find the last node in post[]. The last node is root in postorder
# 2.find the index in inorder
# 3. create a newnode
# 4. recursively call left side of tree and right side of tree
# 5. return root node
class Solution:
    # @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    def buildTree(self, A, B):
        if not B:
            return None
        root_pos=A.index(B[-1])
        newnode=TreeNode(B[-1])
        newnode.left=self.buildTree(A[:root_pos],B[:root_pos])
        newnode.right=self.buildTree(A[root_pos+1:],B[root_pos:-1])
        return newnode