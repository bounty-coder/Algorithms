# Given a Binary Tree. Check whether all of its nodes have 
# the value equal to the sum of their child nodes.

# Input:
#        1
#      /   \
#     4     3
#    /  \
#   5    N
# Output: 0
# Explanation: Here, 1 is the root node
# and 4, 3 are its child nodes. 4 + 3 =
# 7 which is not equal to the value of
# root node. Hence, this tree does not
# satisfy the given conditions.

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # return true if none
        if root is None:
            return 1
        # return 
        if root.left is None and root.right is None:
            return 1
        lft=rgt=0
        # check  if left and right sum equals current node
        if root.left:
            lft=root.left.data
        if root.right:
            rgt=root.right.data
        if root.data==(lft+rgt) and self.isSumProperty(root.left)==1 and self.isSumProperty(root.right)==1:
            return 1
        else:
            return 0
        
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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.isSumProperty(root))
        
