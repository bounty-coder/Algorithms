# Python program to swap the elements of linked list pairwise

# 1. Start from the head node and traverse the list.
# 2. While traversing swap data of each node with its next node’s data. 

class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to pairwise swap elements of a linked list
	def pairwiseSwap(self):
		temp = self.head

		# There are no nodes in linked list
		if temp is None:
			return

		# Traverse furthethr only if there are at least two
		# left
		while(temp and temp.next):

			# If both nodes are same,
			# no need to swap data
			if(temp.data != temp.next.data):

				# Swap data of node with its next node's data
				temp.data, temp.next.data = temp.next.data, temp.data

			# Move temp by 2 to the next pair
			temp = temp.next.next

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Linked list before calling pairWiseSwap() ")
llist.printList()

llist.pairwiseSwap()

print("\nLinked list after calling pairWiseSwap()")
llist.printList()