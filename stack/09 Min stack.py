# Design a Data Structure SpecialStack that supports all the
#  stack operations like push(), pop(), isEmpty(), isFull() 
# and an additional operation getMin() which should return 
# minimum element from the SpecialStack. All these
#  operations of SpecialStack must be O(1). 

# approach 
#use a global help stack to save current minimum element

help_stack=[]
def push(arr, ele):
    # Code here
    global help_stack
    arr.append(ele)
    if len(help_stack)==0:
        help_stack.append(ele)
    elif help_stack[-1]>ele:
        help_stack.append(ele)
    return arr

# Function should pop an element from stack
def pop(arr):
    # Code here
    global help_stack
    
    if help_stack[-1]==arr[-1]:
        help_stack.pop()
    return arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if len(arr)==n:
        return True
    return False

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    if len(arr)==0:
        return True
    return False

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    global help_stack
    
    return help_stack[-1]

arr = list(map(int, input().strip().split()))
n=len(arr)
stack = []
while(not isEmpty(stack)):
    pop(stack)
    
for i in range(n):
    push(stack, arr[i])
print(getMin(n, stack))

# } Driver Code Ends