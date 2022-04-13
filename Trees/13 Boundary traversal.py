# Given a Binary Tree, find its Boundary Traversal

# Left boundary nodes-> Leaf Nodes -> right boundary nodes

# Input:
#         1 
#       /   \
#      2     3  
#     / \   / \ 
#    4   5 6   7
#       / \
#      8   9
   
# Output: 1 2 4 8 9 6 7 3

class Solution:
    def leftsolve(self,root):
        if root:
            if root.left:
                self.stack.append(root.data)
                self.leftsolve(root.left)
            elif root.right:
                self.stack.append(root.data)
                self.leftsolve(root.right)
        
    def rightsolve(self,root):
        if root:
            if root.right:
                self.rightsolve(root.right)
                self.stack.append(root.data)
            elif root.left:
                self.rightsolve(root.left)
                self.stack.append(root.data)
            
    def leavessolve(self,root):
        if root:
            self.leavessolve(root.left)
            
            if (root.left is None) and (root.right is None):
                self.stack.append(root.data)
                
            self.leavessolve(root.right)
            
            
    def printBoundaryView(self, root):
        # Code here
        self.stack=[]
        if root:
            self.stack.append(root.data)
            self.leftsolve(root.left)
            self.leavessolve(root.left)
            self.leavessolve(root.right)
            self.rightsolve(root.right)
        return self.stack

import sys

import sys
sys.setrecursionlimit(100000)
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
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')