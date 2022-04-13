# Construct BST from given preorder traversal

# 1. Create an empty stack.
# 2. Make the first value as root. Push it to the stack.
# 3. Keep on popping while the stack is not empty and the
#  next value is greater than stack’s top value. Make this 
# value as the right child of the last popped node.
#  Push the new node to the stack.
# 4. If the next value is less than the stack’s top value, 
# make this value as the left child of the stack’s top node.
#  Push the new node to the stack.
# 5. Repeat steps 2 and 3 until there are items remaining in pre[].

# A binary tree node
class Node:
	def __init__(self, data = 0):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree :
	# The main function that constructs BST from pre[]
	def constructTree(self, pre, size):

		# The first element of pre[] is always root
		root = Node(pre[0])

		s = []
		# append root
		s.append(root)
		i = 1
		# Iterate through rest of the size-1
		# items of given preorder array
		while ( i < size):
			temp = None
			# Keep on popping while the next value
			# is greater than stack's top value.
			while (len(s) > 0 and pre[i] > s[-1].data):
				temp = s.pop()
			
			# Make this greater value as the right child
			# and append it to the stack
			if (temp != None):
				temp.right = Node(pre[i])
				s.append(temp.right)
			
			# If the next value is less than the stack's top
			# value, make this value as the left child of the
			# stack's top node. append the new node to stack
			else :
				temp = s[-1]
				temp.left = Node(pre[i])
				s.append(temp.left)
			i = i + 1
		
		return root
	
	# A utility function to print
	# inorder traversal of a Binary Tree
	def printInorder(self,node):
		if (node == None):
			return
		
		self.printInorder(node.left)
		print(node.data, end = " ")
		self.printInorder(node.right)

# Driver code
tree = BinaryTree()
pre = [10, 5, 1, 7, 40, 50]
size = len(pre)
root = tree.constructTree(pre, size)
print("Inorder traversal of the constructed tree is ")
tree.printInorder(root)
