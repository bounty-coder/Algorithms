# 1. Create a recursive function recur to reverse the stack.
# 2. Pop the top element in each stack of recursion and hold 
#    the element in function call Stack until we reach the end of the stack.
# 3. While moving back in the recursion tree, push the held element
#  of each recursion call stack at the bottom of the stack.

# Below is a recursive function
# that inserts an element
# at the bottom of a stack.
def insertAtBottom(stack, item):
	if isEmpty(stack):
		push(stack, item)
	else:
		temp = pop(stack)
		insertAtBottom(stack, item)
		push(stack, temp)

# Below is the function that
# reverses the given stack
# using insertAtBottom()
def reverse(stack):
	if not isEmpty(stack):
		temp = pop(stack)
		reverse(stack)
		insertAtBottom(stack, temp)

# Below is a complete running
# program for testing above
# functions.

# Function to check if
# the stack is empty
def isEmpty( stack ):
	return len(stack) == 0

# Function to push an
# item to stack
def push( stack, item ):
	stack.append( item )

# Function to pop an
# item from stack
def pop( stack ):

	# If stack is empty
	# then error
	if(isEmpty( stack )):
		print("Stack Underflow ")
		exit(1)

	return stack.pop()

# Function to print the stack
def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end = ' ')
	print()

# Driver Code

stack = []
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)

reverse(stack)

print("Reversed Stack ")
prints(stack)