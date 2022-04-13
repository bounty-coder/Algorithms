# Given a binary tree, flatten it into linked list in-place.
# Usage of auxiliary data structure is not allowed. After flattening,
#  left of each node should point to NULL and right 
# should contain next node in preorder.

# Input : 
#           1
#         /   \
#        2     5
#       / \     \
#      3   4     6

# Output :  1 2 3 4 5 6 

# Traverse recursively root->right-> left (right preorder)
# Recursively look for the node with no grandchildren
#  and both left and right child in the left sub-tree.
# temp= node.right  then node.right=node.left
#Insert temp in first node NULL on right of node by node=node->right.
# Repeat until it is converted to linked list. 

class Solution:
    def flatten(self, root):
        #code here
        if root is None or (root.left is None and root.right is None):
            return
        if root.left:
            self.flatten(root.left)
            
            tmpright=root.right
            root.right=root.left
            root.left=None
            
            t=root.right
            while t.right!=None:
                t=t.right
                
            t.right=tmpright
        
        self.flatten(root.right)

#{ 
#  Driver Code Starts

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
def inorder(root):
    if root == None:
        return 
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        root = buildTree(s)
        ob = Solution()
        ob.flatten(root)
        inorder(root)
                
        print()
            
# } Driver Code Ends