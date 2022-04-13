# Method 2 (Using Single Traversal) 
# The idea is to traverse the tree starting from the root. 
# If any of the given keys (n1 and n2) matches with the root,
# then the root is LCA (assuming that both keys are present). 
# If the root doesn’t match with any of the keys, 
# we recur for the left and right subtree. 
# The node which has one key present in its left subtree and
# the other key present in the right subtree is the LCA. 
# If both keys lie in the left subtree, 
# then the left subtree has LCA also, otherwise,
# LCA lies in the right subtree.

# Python program to find LCA of n1 and n2 using one
# traversal of Binary tree
class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

    def contains(self,root,n):
        if root is None:
            return False
        if root.val==n:
            return True
        return self.contains(root.left,n) or self.contains(root.right,n)

    def lcak(self, A, B, C):
        if A is None:
            return None
    
        if A.val==B and A.val==C:
            return A.val
        
        lca1=self.lcak(A.left,B,C)
        lca2=self.lcak(A.right,B,C)

        if lca1 and lca2:
            return A.val 
        if lca1:
            return lca1 
        if lca2:
            return lca2
        return None
    
    def lca(self,A,B,C):
        if self.contains(A,B) and self.contains(A,C):
            return -1
        x=self.lcak(A,B,C)
        if x:
            return x
        return -1

# Let us create a binary tree given in the above example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
s=Solution()
print ("LCA(4,5) = ", s.lca(root, 4, 5).key)
print ("LCA(4,6) = ", s.lca(root, 4, 6).key)
print ("LCA(3,4) = ", s.lca(root, 3, 4).key)
print ("LCA(2,4) = ", s.lca(root, 2, 4).key)