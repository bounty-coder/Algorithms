# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally 
# identical and the nodes have the same value.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# JUST TRAVERSE AND CHECK BOTH
class Solution:
	def inorder(self,root):
		if not root:
			return []
		return self.inorder(root.left) + [root.val] +self.inorder(root.right)
	def isSameTree(self, A, B):
		stack1=self.inorder(A)
		stack2=self.inorder(B)
		if stack1==stack2:
			return 1
		return 0