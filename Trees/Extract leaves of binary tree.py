# Python program to extract leaf nodes from binary tree
# using double linked list


# Let the following be input binary tree
#         1
#      /     \
#     2       3
#    / \       \
#   4   5       6
#  / \         / \
# 7   8       9   10


# Output:
# Doubly Linked List
# 785910

# Modified Tree:
#         1
#      /     \
#     2       3
#    /         \
#   4           6 


# A binary tree node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Main function which extracts all leaves from given Binary Tree.
# The function returns new root of Binary Tree (Note that
# root may change if Binary Tree has only one node).
# The function also sets *head_ref as head of doubly linked list.
# left pointer of tree is used as prev in DLL
# and right pointer is used as next
def extractLeafList(root):
	
	# Base Case
	if root is None:
		return None

	if root.left is None and root.right is None:
		# This node is going to be added to doubly linked
		# list of leaves, set pointer of this node as
		# previous head of DLL. We don't need to set left
		# pointer as left is already None
		root.right = extractLeafList.head
		
		# Change the left pointer of previous head
		if extractLeafList.head is not None:
			extractLeafList.head.left = root

		# Change head of linked list
		extractLeafList.head = root
		
		return None # Return new root

	# Recur for right and left subtrees
	root.right = extractLeafList(root.right)
	root.left = extractLeafList(root.left)
	
	return root

# Utility function for printing tree in InOrder
def printInorder(root):
	if root is not None:
		printInorder(root.left)
		print (root.data,end=" ")
		printInorder(root.right)


def printList(head):
	while(head):
		if head.data is not None:
			print (head.data,end=" ")
		head = head.right

# Driver program to test above function
extractLeafList.head = Node(None)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

print ("Inorder traversal of given tree is:")
printInorder(root)

root = extractLeafList(root)

print ("\nExtract Double Linked List is:")
printList(extractLeafList.head)

print ("\nInorder traversal of modified tree is:")
printInorder(root)
