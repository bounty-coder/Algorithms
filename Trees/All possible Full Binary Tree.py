# Print all possible N-nodes Full Binary Trees

# As for full binary tree there must be odd no. of nodes
# The simplest way to solve the problem is to use recursion and check for each subtree
# if there is a odd number of nodes or not because a full binary tree has odd nodes.

# Initialize a hashMap, say hm that stores all the Full Binary Tree.
# Create a function, say allPossibleBFT with the parameter 
# as N by performing the following steps:
# Create a List, say list containing the class nodes.
# If N =1, then add nodes(0, NULL, NULL) in the list.
# Now check if N is odd, then Iterate in the range [0, N-1] using the variable x
# and perform the following steps:
# Initialize a variable, say y as N – 1 – x.
# Recursively call the function allPossibleBFT with x as the parameter 
# and assign it to the node left.
# Recursively call the function allPossibleBFT with y as the 
# parameter inside the above call and assign it to the node right.
# Now create a new Node with parameters as (0, NULL, NULL).
# Assign Node.left as left and Node.right as right.
# Add Node to the List.
# After performing the above steps, insert list in the hashMap hm.

# Python3 program for the above approach
import sys
 
# Class for creating node and
# its left and right child
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
 
# Function to traverse the tree and add all
# the left and right child in the list al
def display(node, al):
   
    # If node = null then terminate the function
    if (node == None):
        return
       
    # If there is left child of Node node
    # then insert it into the list al
    if (node.left != None):
        al.append(node.left.data)
         
    # Otherwise insert null in the list
    else:
        al.append(-sys.maxsize)
      
    # Similarly, if there is right child
    # of Node node then insert it into
    # the list al
    if (node.right != None):
        al.append(node.right.data)
    # Otherwise insert null
    else:
        al.append(-sys.maxsize)
     
    # Recursively call the function
    # for left child and right child
    # of the Node node
    display(node.left, al)
    display(node.right, al)
 
# Save tree for all n before recursion.
hm = {}
def allPossibleFBT(n):
    # Check whether tree exists for given n value or not.
    if n not in hm:
       
        # Create a list containing nodes
        List = []
         
        # If N=1, Only one tree can exist
        # i.e. tree with root.
        if (n == 1):
            List.append(Node(0, None, None))
         
        # Check if N is odd because binary full
        # tree has N nodes
        elif (n % 2 == 1):
           
            # Iterate through all the nodes that
            # can be in the left subtree
            for x in range(n):
               
                # Remaining Nodes belongs to the
                # right subtree of the node
                y = n - 1 - x
                 
                # Iterate through all left Full Binary Tree
                #  by recursively calling the function
                xallPossibleFBT = allPossibleFBT(x)
                yallPossibleFBT = allPossibleFBT(y)
                for Left in range(len(xallPossibleFBT)):
                   
                    # Iterate through all the right Full
                    # Binary tree by recursively calling
                    # the function
                    for Right in range(len(yallPossibleFBT)):
                       
                        # Create a new node
                        node = Node(0, None, None)
                         
                        # Modify the left node
                        node.left = xallPossibleFBT[Left]
                         
                        # Modify the right node
                        node.right = yallPossibleFBT[Right]
                         
                        # Add the node in the list
                        List.append(node)
         
        #Insert tree in Dictionary.
        hm[n] = List
    return hm[n]
 
# Given Input
n = 7
 
# Function Call
List = allPossibleFBT(n)
 
# Print all possible binary full trees
for root in range(len(List)):
    al = []
    al.append(List[root].data)
    display(List[root], al)
     
    print("[", end = "")
     
    for i in range(len(al)):
        if(i != len(al) - 1):
            if(al[i]==-sys.maxsize):
                print("null, ", end = "")
            else:
                print(al[i], end = ", ")
        else:
            if(al[i]==-sys.maxsize):
                print("null]", end = "")
            else:
                print(al[i], end =  "]")
    print()